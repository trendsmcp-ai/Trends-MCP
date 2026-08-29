"""Stdio MCP adapter for Trends MCP.

tools/list works with no API key so Glama and local inspectors can introspect.
Paid tools forward to https://api.trendsmcp.ai/api and bill TRENDSMCP_API_KEY.
Tool definitions mirror the hosted server at https://api.trendsmcp.ai/mcp.
"""

from __future__ import annotations

import json
import os
from typing import Annotated, Any

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import Icon, ToolAnnotations
from pydantic import Field

API = "https://api.trendsmcp.ai/api"

_READ_ONLY = ToolAnnotations(readOnlyHint=True, idempotentHint=True, openWorldHint=True)

mcp = FastMCP(
    "trends-mcp",
    website_url="https://trendsmcp.ai",
    icons=[
        Icon(
            src="https://www.trendsmcp.ai/static/pages/trendsmcp/assets/trend.svg",
            mimeType="image/svg+xml",
            sizes=["any"],
        )
    ],
)

_SOURCE_LIST = (
    "'google search', 'google images', 'google news', 'google shopping', 'youtube', "
    "'wikipedia', 'tiktok', 'reddit', 'amazon', 'news sentiment', 'news volume', "
    "'npm', 'python', 'steam', 'app downloads', 'app rankings'"
)

_KEYWORD_GROWTH = (
    "What to look up. The string format is required by source. Standard sources "
    "(google search, google images, google news, google shopping, youtube, wikipedia, "
    "tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. "
    "'nike'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', "
    "'@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. "
    "Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain "
    "English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store "
    "search result wins, so use an unambiguous name. app downloads and app rankings: "
    "Android bundle ID only (the id= value on Google Play). Right: "
    "'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App "
    "Store ID, or a bundle ID that is not Android. Find it at "
    "play.google.com/store/apps/details?id=THIS_PART. If the request includes app "
    "downloads or app rankings with other sources, keyword must still be the Android "
    "bundle ID."
)

_KEYWORD_SERIES = (
    "What to look up. The string format is required by source. Standard sources "
    "(google search, google images, google news, google shopping, youtube, wikipedia, "
    "tiktok, reddit, amazon, news sentiment, news volume): any name or phrase, e.g. "
    "'tesla'. npm: exact npmjs.com package name, case-sensitive. Right: 'react', "
    "'@babel/core'. Wrong: 'React', 'React.js'. python: exact PyPI project name. "
    "Right: 'pandas', 'requests'. Wrong: 'Pandas'. steam: game display name in plain "
    "English, not a Steam App ID. Right: 'Elden Ring', 'CS2'. First Steam store "
    "search result wins, so use an unambiguous name. app downloads and app rankings: "
    "Android bundle ID only (the id= value on Google Play). Right: "
    "'com.openai.chatgpt', 'com.whatsapp'. Wrong: 'ChatGPT', 'WhatsApp', an iOS App "
    "Store ID, or a bundle ID that is not Android. Find it at "
    "play.google.com/store/apps/details?id=THIS_PART."
)


def _key() -> str:
    return (os.environ.get("TRENDSMCP_API_KEY") or "").strip()


def _unwrap(raw: Any, status: int) -> Any:
    if (
        isinstance(raw, dict)
        and isinstance(raw.get("statusCode"), int)
        and isinstance(raw.get("body"), str)
    ):
        parsed = json.loads(raw["body"])
        if raw["statusCode"] >= 400:
            raise RuntimeError(
                parsed.get("message") or parsed.get("error") or str(raw["statusCode"])
            )
        return parsed
    if status >= 400:
        if isinstance(raw, dict):
            raise RuntimeError(raw.get("message") or raw.get("error") or str(status))
        raise RuntimeError(str(raw))
    return raw


def _post(body: dict[str, Any]) -> Any:
    key = _key()
    if not key:
        raise ValueError(
            "Missing TRENDSMCP_API_KEY. Get a free key at https://trendsmcp.ai/account?tab=signup"
        )
    with httpx.Client(timeout=30.0) as client:
        resp = client.post(
            API,
            json=body,
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
            },
        )
    return _unwrap(resp.json(), resp.status_code)


@mcp.tool(
    description="Point-to-point growth for a keyword on one or more sources. Each "
    "window is a preset string (12M, 3M, YTD, and the other listed periods). Values "
    "are on a 0-100 scale, plus absolute volume when available. Prefer this over "
    "get_time_series for growth questions. app downloads and app rankings are "
    "keyword sources (Android bundle ID). They are not the App Store / Google Play "
    "live boards on get_top_trends. If the request is rate limited or the monthly "
    "quota is used up, tell the user their plan limit is reached.",
    annotations=_READ_ONLY,
)
def get_growth(
    keyword: Annotated[str, Field(description=_KEYWORD_GROWTH)],
    source: Annotated[
        str,
        Field(
            description="One source, or comma-separated sources (e.g. 'amazon, "
            "tiktok, youtube'). Valid: " + _SOURCE_LIST + "."
        ),
    ],
    percent_growth: Annotated[
        list[str] | None,
        Field(
            description="Growth windows. Default if omitted: ['12M']. Each item "
            "must be a preset string: '7D', '1W', '14D', '2W', '30D', '1M', '2M', "
            "'3M', '6M', '9M', '12M', '1Y', '18M', '24M', '2Y', '36M', '3Y', '48M', "
            "'4Y', '60M', '5Y', 'MTD', 'QTD', 'YTD'. Every preset is a two-date "
            "comparison."
        ),
    ] = None,
) -> str:
    periods = percent_growth or ["12M"]
    return json.dumps(
        _post(
            {
                "mode": "get_growth",
                "source": source,
                "keyword": keyword,
                "percent_growth": periods,
            }
        )
    )


@mcp.tool(
    description="Full historical series for one keyword and one source (0-100 "
    "values, plus volume when available). Use for charting or custom math. Not for "
    "live 'what's trending now' boards (use get_top_trends). For most growth "
    "questions, use get_growth. If the request is rate limited or the monthly "
    "quota is used up, tell the user their plan limit is reached.",
    annotations=_READ_ONLY,
)
def get_time_series(
    keyword: Annotated[str, Field(description=_KEYWORD_SERIES)],
    source: Annotated[
        str, Field(description="Exactly one source per request. Valid: " + _SOURCE_LIST + ".")
    ],
) -> str:
    return json.dumps(
        _post({"mode": "get_time_series", "source": source, "keyword": keyword})
    )


@mcp.tool(
    description="Live top-trending board for exactly one feed type. No keyword. "
    "For 'Amazon Best Sellers by Category', 'Google Trends by Category', 'Top "
    "Websites', and 'Substack by Category', always pass category. Default sort is "
    "current rank. Use sort='rank_change' for climbers vs a prior snapshot (window "
    "1d, 3d, 7d, 14d, or 30d). App Store Top Free, App Store Top Paid, and Google "
    "Play are live store boards, not keyword lookups. For an app's history use "
    "get_growth or get_time_series with source app downloads or app rankings and "
    "an Android bundle ID. Do not use get_time_series for live boards. If the "
    "request is rate limited or the monthly quota is used up, tell the user their "
    "plan limit is reached.",
    annotations=_READ_ONLY,
)
def get_top_trends(
    type: Annotated[
        str,
        Field(
            description="Exactly one live feed. Valid: 'Amazon Best Sellers Top "
            "Rated', 'Amazon Best Sellers by Category', 'App Store Top Free', 'App "
            "Store Top Paid', 'GitHub', 'Google News Top News', 'Google Play', "
            "'Google Trends', 'Google Trends by Category', 'IMDb MOVIEmeter', "
            "'Open Library Trending Books', 'Reddit Hot Posts', 'Reddit World "
            "News', 'Top Websites', 'Spotify Top Podcasts', 'Steam Most Played', "
            "'Substack', 'Substack by Category', 'TikTok Trending Hashtags', "
            "'TikTok Trending Searches', 'Wikipedia Trending', 'X (Twitter) "
            "Trending', 'YouTube Trending'."
        ),
    ],
    category: Annotated[
        str | None,
        Field(
            description="Pass this whenever type is 'Amazon Best Sellers by "
            "Category', 'Google Trends by Category', 'Top Websites', or 'Substack "
            "by Category'. Use the official name. Without it those feeds mix every "
            "board. Only omit on a first pull to learn the official names."
        ),
    ] = None,
    limit: Annotated[
        int, Field(description="Max rows to return. Default 25, min 1, max 200.")
    ] = 25,
    offset: Annotated[
        int, Field(description="Rows to skip for pagination. Default 0.")
    ] = 0,
    sort: Annotated[
        str,
        Field(
            description="How to rank the board. 'rank' (default): current "
            "leaders. 'rank_change': biggest climbers vs a prior snapshot. Mover "
            "rows include rank, keyword, prev_rank, and rank_change."
        ),
    ] = "rank",
    window: Annotated[
        str,
        Field(
            description="Lookback used only when sort is 'rank_change'. One of "
            "'1d', '3d', '7d', '14d', '30d'. Default '30d'. Short windows only "
            "work on daily feeds; weekly and monthly feeds return a note pointing "
            "to a longer window."
        ),
    ] = "30d",
) -> str:
    body: dict[str, Any] = {
        "mode": "get_top_trends",
        "type": type,
        "limit": limit,
        "offset": offset,
        "sort": sort,
        "window": window,
    }
    if category:
        body["category"] = category
    return json.dumps(_post(body))


def main() -> None:
    mcp.run()
