"""Stdio MCP adapter for Trends MCP.

tools/list works with no API key so Glama and local inspectors can introspect.
Paid tools forward to https://api.trendsmcp.ai/api and bill TRENDSMCP_API_KEY.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API = "https://api.trendsmcp.ai/api"

mcp = FastMCP("trends-mcp")


def _key() -> str:
    return (os.environ.get("TRENDSMCP_API_KEY") or os.environ.get("API_KEY") or "").strip()


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


@mcp.tool()
def get_trends(keyword: str, source: str = "google search", data_mode: str = "weekly") -> str:
    """Return about 5 years of weekly or daily interest for one keyword on one source, 0-100.

    Use for history and whether interest is durable. Do not use for today's
    leaderboard (get_top_trends) or percent change (get_growth).
    Requires TRENDSMCP_API_KEY. Counts against the key quota. Cap returns 429 rate_limited.

    source: google search, google images, google news, google shopping, youtube,
    tiktok, reddit, amazon, wikipedia, news volume, news sentiment, app downloads,
    app rankings, npm, steam.
    """
    return json.dumps(
        _post(
            {
                "mode": "get_time_series",
                "source": source,
                "keyword": keyword,
                "data_mode": data_mode,
            }
        )
    )


@mcp.tool()
def get_growth(
    keyword: str,
    source: str = "google search",
    percent_growth: str = "3M,1Y",
) -> str:
    """Return percent change for a keyword over one or more windows (7D to 5Y).

    source may be a comma-separated list to compare platforms in one call.
    Use instead of get_trends when you need growth, not the raw series.
    Requires TRENDSMCP_API_KEY. percent_growth: comma-separated presets such as 3M,1Y,12M.
    """
    periods = [p.strip() for p in percent_growth.split(",") if p.strip()]
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


@mcp.tool()
def get_top_trends(type: str = "Google Trends", limit: int = 20) -> str:
    """Live leaderboard. No keyword. Use for what is trending on a platform right now.

    Do not use for a specific keyword's history (get_trends) or growth (get_growth).
    Requires TRENDSMCP_API_KEY. type examples: Google Trends, TikTok Trending Hashtags,
    YouTube, Reddit Hot, Amazon Best Sellers, GitHub Trending Repos.
    """
    return json.dumps(_post({"mode": "get_top_trends", "type": type, "limit": limit}))


def main() -> None:
    mcp.run()
