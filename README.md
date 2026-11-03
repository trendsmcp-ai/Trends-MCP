<div align="center">

<!-- mcp-name: ai.trendsmcp/trends -->

<img src="https://www.trendsmcp.ai/static/pages/trendsmcp/assets/trend.svg" width="72" alt="Trends MCP logo">

# Trends MCP

Live trend data for AI agents: 53 data sets from 27 platforms, including Google, TikTok, YouTube, Amazon, Reddit, Pinterest, Instagram and X. One MCP connection, one API key.

[![PyPI](https://img.shields.io/pypi/v/trends-mcp-server)](https://pypi.org/project/trends-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/trendsmcp-ai/Trends-MCP/actions/workflows/ci.yml/badge.svg)](https://github.com/trendsmcp-ai/Trends-MCP/actions/workflows/ci.yml)
[![MCP](https://img.shields.io/badge/MCP-remote%20%2B%20stdio-blue)](https://modelcontextprotocol.io)
[![Free tier](https://img.shields.io/badge/Free-100%20req%2Fmo-orange)](https://www.trendsmcp.ai/pricing)
[![Glama](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP/badges/score.svg)](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP)

[Get a free API key](https://www.trendsmcp.ai/account) · [Docs](https://www.trendsmcp.ai/docs) · [Pricing](https://www.trendsmcp.ai/pricing) · [Data catalog](https://www.trendsmcp.ai/data-catalog) · [PyPI](https://pypi.org/project/trends-mcp-server/) · [Glama](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP)

</div>

```
You: Using TrendsMCP, compare 6-month growth for GLP-1 on Google, TikTok, and Amazon.

Agent: Google Search  +84%
       TikTok         +212%
       Amazon         +61%
```

5 tools plus a free usage check. History, growth, live boards, and what people are saying right now. Normalized 0–100 where the source supports it. No per-platform keys. No scraping on your side.

## Quick install

Same four clients as the site hero. [Get a free key](https://www.trendsmcp.ai/account) first (100 req/mo). Claude and ChatGPT sign you in with OAuth. Cursor and VS Code: click, then put your key from `/account` if the deeplink used a placeholder.

<p align="center">
  <a href="https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Trends%20MCP&connectorUrl=https%3A%2F%2Fwww.trendsmcp.ai%2Fmcp"><img src="https://img.shields.io/badge/Add_to-Claude-DA7756?style=for-the-badge&logo=claude&logoColor=white" alt="Add to Claude"></a>
  <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=trends-mcp&config=eyJ1cmwiOiJodHRwczovL2FwaS50cmVuZHNtY3AuYWkvbWNwIiwidHJhbnNwb3J0IjoiaHR0cCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciBZT1VSX0FQSV9LRVkifX0%3D"><img src="https://img.shields.io/badge/Add_to-Cursor-000000?style=for-the-badge" alt="Add to Cursor"></a>
  <a href="https://chatgpt.com/plugins#settings/Connectors?create-connector=true&redirectAfter=%2Fplugins"><img src="https://img.shields.io/badge/Add_to-ChatGPT-10A37F?style=for-the-badge" alt="Add to ChatGPT"></a>
  <a href="https://www.trendsmcp.ai/account"><img src="https://img.shields.io/badge/Add_to-VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="Add to VS Code"></a>
</p>

| Client | After you click |
|---|---|
| **Claude** | Connector name and URL are prefilled (`https://www.trendsmcp.ai/mcp`). Confirm, then authorize. |
| **Cursor** | Approve the MCP install. Replace `YOUR_API_KEY` if prompted. |
| **ChatGPT** | In ChatGPT on the web: Plugins → + → Add custom MCP server. URL `https://www.trendsmcp.ai/mcp`, authentication OAuth, then create, install and sign in. |
| **VS Code** | Sign in on the account page and use the **VS Code** button so the key is included. |

Then ask: `Using TrendsMCP, what's trending on Google right now?`

**[Tools](#tools)** · **[Sources](#keyword-sources)** · **[Boards](#live-boards)** · **[REST](#rest-api)** · **[Install in other clients](#install-in-other-clients)**

---

## What this is

Hosted MCP at `https://api.trendsmcp.ai/mcp`. Same Bearer key for `POST https://api.trendsmcp.ai/api`. This repo also has a stdio adapter for Glama and local hosts.

| Tool | What it does | Cost |
|---|---|---|
| `get_time_series` | Full history for one topic. About five years of weekly history for one keyword on one source, as a 0 to 100 index plus volume where the source has it. | 1 request per call |
| `get_growth` | How fast something is rising. Point-to-point growth over one or more windows, on one source or several in the same call. | 1 request per call, every window included |
| `get_top_trends` | What's moving right now. A live ranked board with no keyword: the current leaders, or the biggest climbers against an earlier snapshot. | MCP: 1 request per 10 rows, at most 10 per call. REST: 1 request per call |
| `get_context` | What people are saying. What people are posting, reading and betting about a keyword right now: posts, videos, stories, comments and markets from each source, with engagement. | MCP: 1 request per source, at most 5 per call. REST: one source per call, 1 request |
| `get_top_posts` | Top posts for one hashtag. Live top posts for one hashtag, fetched on every call. Business plan. | 1 request per call |
| `get_usage` | Your plan, requests used and left, reset date. MCP only. | Free |

`get_top_posts` is on the Business plan. Every other tool works on every plan, Free included.

---

## Install in other clients

Replace `YOUR_API_KEY` with the key from [your account](https://www.trendsmcp.ai/account).

<details>
<summary>Claude Code</summary>

```bash
claude mcp add --scope user --transport http trends-mcp https://api.trendsmcp.ai/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```
</details>

<details>
<summary>Cursor (manual)</summary>

`~/.cursor/mcp.json` (Windows: `%USERPROFILE%\.cursor\mcp.json`)

```json
{
  "mcpServers": {
    "trends-mcp": {
      "url": "https://api.trendsmcp.ai/mcp",
      "transport": "http",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```
</details>

<details>
<summary>VS Code / Copilot (manual JSON)</summary>

`.vscode/mcp.json` or Command Palette → MCP: Add Server. Prefer the account-page VS Code button so the key is wired for you.

```json
{
  "servers": {
    "trends-mcp": {
      "type": "http",
      "url": "https://api.trendsmcp.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```
</details>

<details>
<summary>Windsurf</summary>

Uses `serverUrl`, not Cursor’s `url` + `transport`. File: `~/.codeium/windsurf/mcp_config.json`.

```json
{
  "mcpServers": {
    "trends-mcp": {
      "serverUrl": "https://api.trendsmcp.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```
</details>

<details>
<summary>Cline</summary>

Remote server, type **exactly** `streamableHttp`. See [llms-install.md](llms-install.md).

```json
{
  "mcpServers": {
    "trends-mcp": {
      "type": "streamableHttp",
      "url": "https://api.trendsmcp.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" },
      "disabled": false
    }
  }
}
```
</details>

<details>
<summary>Claude Desktop (no native HTTP)</summary>

```json
{
  "mcpServers": {
    "trends-mcp": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://api.trendsmcp.ai/mcp",
        "--header", "Authorization:${AUTH_HEADER}"
      ],
      "env": { "AUTH_HEADER": "Bearer YOUR_API_KEY" }
    }
  }
}
```
</details>

<details>
<summary>Claude.ai custom connector</summary>

Settings → Connectors → add `https://www.trendsmcp.ai/mcp`. This path uses OAuth on `www.trendsmcp.ai`. Do not put a Bearer key in that connector config.
</details>

<details>
<summary>Stdio (this repo / Glama)</summary>

Hosted HTTP is the product default and has every tool. This stdio adapter exposes `get_time_series`, `get_growth` and `get_top_trends`; use the hosted server for `get_context`, `get_top_posts` and `get_usage`. It lists tools with no key; calls need `TRENDSMCP_API_KEY` and bill the same quota.

```bash
pip install -e .
python -m trends_mcp_server
```

```json
{
  "mcpServers": {
    "trends-mcp": {
      "command": "python",
      "args": ["-m", "trends_mcp_server"],
      "env": { "TRENDSMCP_API_KEY": "YOUR_API_KEY" }
    }
  }
}
```
</details>

<details>
<summary>Prompt tip</summary>

Say “using TrendsMCP” so the model picks these tools instead of web search. More clients: [docs](https://www.trendsmcp.ai/docs).
</details>

---

## Tools

Always-current parameter lists: [docs](https://www.trendsmcp.ai/docs) and [data catalog](https://www.trendsmcp.ai/data-catalog.md). Same names on MCP and REST (`"mode": "<tool>"`).

### `get_time_series`

About five years of weekly history for **one** `source` + `keyword`, as a 0–100 index plus volume where the source has it.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | Format depends on source ([table below](#keyword-sources)) |
| `source` | yes | Exactly one keyword source |
| `country` | no | ISO code (`US`, `GB`, `JP`) on Google, YouTube, TikTok and Pinterest sources. Google defaults to worldwide |
| `resolution` | no | Google and YouTube sources: `weekly` (about 5 years, default) or `daily` (last 90 days) |
| `language` | no | Wikipedia edition (`en`, `de`, `ja`). Default `en` |

### `get_growth`

Point-to-point percent change. Several windows in one call still count as **one** request.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | Same formats as `get_time_series` |
| `source` | yes | One source, or several separated by commas (`Google Search, TikTok, Amazon`) |
| `percent_growth` | no | Default `["12M"]`. Presets below, or a custom date-range object (REST) |

Any number with D, W, M or Y up to 5 years, plus `MTD` `QTD` `YTD`. Common: `7D` `1W` `14D` `2W` `30D` `1M` `2M` `3M` `6M` `9M` `12M` `1Y` `18M` `24M` `2Y` `36M` `3Y` `48M` `4Y` `60M` `5Y` `MTD` `QTD` `YTD`.

### `get_top_trends`

Live ranked board. **No keyword.** `type` must match the board name exactly (including capitals).

| Argument | Required | Notes |
|---|---|---|
| `type` | yes | See [live boards](#live-boards) |
| `limit` | no | 1 to 200. Default 25 |
| `offset` | no | Rows to skip |
| `sort` | no | `rank` (default) or `rank_change` for climbers |
| `window` | no | With `rank_change`: `1d` `3d` `7d` `14d` `30d`. Default `30d` |
| `category` | for some types | The `by Category` boards and Top Websites. Names in the [data catalog](https://www.trendsmcp.ai/data-catalog.md) |
| `country` | no | Google Trends, Pinterest, TikTok hashtags, X and YouTube boards. Default `US` |

MCP bills 1 request per 10 rows (at most 10 per call). REST bills 1 request per call. Free plan: top 10, about 24 hours behind.

### `get_context`

What people are posting, reading and betting about a keyword right now: posts, videos, stories, comments and markets, with engagement.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | Any name or phrase |
| `source` | yes | One source, or up to 5 separated by commas (MCP). REST: one per call |
| `days` | no | Look back 1 to 30 days. Default 7 |
| `limit` | no | Items per source, 1 to 20. Default 10 |
| `comments` | no | Top comments for the first N items (0 to 5, default 2) |

Sources: `News`, `YouTube`, `TikTok`, `Instagram`, `X`, `Reddit`, `Bluesky`, `Hacker News`, `Polymarket`, `GitHub`. MCP bills 1 request per source.

### `get_top_posts`

Live top posts for one hashtag, fetched on every call. **Business plan.** 1 request per call.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | The hashtag, with or without `#` |
| `source` | yes | `TikTok` or `Instagram` |
| `limit` | no | 1 to 20. Default 20 |

### `get_usage`

Free, MCP only. Your plan, requests used and left this month, and the reset date.

---

## Prompts that route correctly

```
Using TrendsMCP, what's trending on Google right now?
Using TrendsMCP, why is Clayface trending? Show me the posts and stories behind it.
Using TrendsMCP, compare 6-month growth for creatine gummies on Google, TikTok, and Amazon.
Using TrendsMCP, show Google Search history for protein soda.
Via TrendsMCP, pull npm download history for langchain.
Using TrendsMCP, what are people saying about the Nintendo Switch 2 on Reddit and YouTube?
Via TrendsMCP, Android downloads for com.openai.chatgpt.
Using TrendsMCP, fastest-climbing Amazon best sellers in Toys Games this week.
```

---

## Keyword sources

`source` on `get_time_series` and `get_growth` (14).

| `source` | Pass as `keyword` | Extra options |
|---|---|---|
| `Google Search` | Any name or phrase, e.g. `electric vehicles` | `country`, `resolution` |
| `Google Images` | Any name or phrase, e.g. `electric vehicles` | `country`, `resolution` |
| `Google News` | Any name or phrase, e.g. `electric vehicles` | `country`, `resolution` |
| `Google Shopping` | Any name or phrase, e.g. `running shoes` | `country`, `resolution` |
| `YouTube` | Any name or phrase, e.g. `stanley cup` | `country`, `resolution` |
| `Wikipedia` | Any name or phrase, e.g. `Bitcoin` | `language` |
| `TikTok` | Any name or phrase, e.g. `booktok` | `country` |
| `Amazon` | Any name or phrase, e.g. `air fryer` | - |
| `Pinterest` | Any name or phrase, e.g. `matcha` | `country` |
| `npm` | Exact npmjs.com package name, case-sensitive, e.g. `langchain` | - |
| `Python` | Exact PyPI project name, e.g. `pandas` | - |
| `Steam` | Game display name in plain English, not a Steam App ID, e.g. `Elden Ring` | - |
| `App Downloads` | Android bundle ID only (the id= value on Google Play), e.g. `com.openai.chatgpt` | - |
| `App Rankings` | Android bundle ID only (the id= value on Google Play), e.g. `com.openai.chatgpt` | - |

`source: "Google Trends"` is invalid. Use `Google Search` for history and `type: "Google Trends"` for the live board.

---

## Live boards

`type` on `get_top_trends` (27). Copy the name exactly.

- **Amazon:** `Amazon Best Sellers Top Rated`, `Amazon Best Sellers by Category`
- **App Store:** `App Store Top Free`, `App Store Top Paid`
- **GitHub:** `GitHub`
- **Google News:** `Google News Top News`
- **Google Play:** `Google Play`
- **Google Trends:** `Google Trends`, `Google Trends by Category`
- **IMDb:** `IMDb MOVIEmeter`
- **Open Library:** `Open Library Trending Books`
- **Pinterest:** `Pinterest Trending`, `Pinterest Trending by Category`
- **Polymarket:** `Polymarket Top Markets`
- **Reddit:** `Reddit Hot Posts`, `Reddit World News`
- **Web:** `Top Websites`
- **Spotify:** `Spotify Top Podcasts`
- **Steam:** `Steam Most Played`
- **Substack:** `Substack`, `Substack by Category`
- **TikTok:** `TikTok Trending Hashtags`, `TikTok Trending Hashtags by Category`, `TikTok Trending Searches`
- **Wikipedia:** `Wikipedia Trending`
- **X:** `X (Twitter) Trending`
- **YouTube:** `YouTube Trending`

Category names per board: [data catalog](https://www.trendsmcp.ai/data-catalog.md).

---

## REST API

```bash
curl -sS -X POST https://api.trendsmcp.ai/api \
  -H "Authorization: Bearer $TRENDSMCP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_top_trends","type":"Google Trends","limit":5}'
```

```python
import os, requests

r = requests.post(
    "https://api.trendsmcp.ai/api",
    headers={"Authorization": f"Bearer {os.environ['TRENDSMCP_API_KEY']}"},
    json={"mode": "get_growth", "source": "google search", "keyword": "bitcoin", "percent_growth": ["3M", "12M"]},
)
print(r.json())
```

Python client: [`pip install trendsmcp`](https://pypi.org/project/trendsmcp/).

---

## Limits and errors

| Plan | Requests / month | Top trends rows | Price / month |
|---|---|---|---|
| Free | 100 | Top 10, 24h delay | $0 |
| Starter | 1,000 | Top 25 | $19 |
| Pro | 5,000 | Top 100 | $49 |
| Business | 25,000 | Full board | $199 |

Yearly billing: Starter $16/mo, Pro $39/mo, Business $159/mo. Every plan reads every data set; Top Posts is on Business. Failed calls are free.

**Pay as you go:** one-time credit packs, no subscription ($15 for 600, $49 for 2,500, $199 for 12,000 credits). 1 credit = 1 request. Credits never expire and are used after a plan's monthly requests run out. [Pricing](https://www.trendsmcp.ai/pricing).

What one request is:

- `get_time_series`: one source + keyword
- `get_growth`: one keyword, every window in the call included
- `get_top_trends`: MCP 1 per 10 rows (max 10 per call); REST 1 per call
- `get_context`: MCP 1 per source (max 5 per call); REST one source per call
- `get_top_posts`: 1 per call
- `get_usage`: free

| Status | Meaning |
|---|---|
| 400 | Bad or missing `source` / `type` / field, or no growth window could be calculated |
| 401 | Missing key (HTTP) |
| 403 | Invalid key (HTTP), or the tool needs a higher plan (`plan_required`) |
| 404 | No data for that keyword + source |
| 502 | Upstream source did not answer (`source_unavailable`) |
| 500 | Internal error (body has a `request_id`) |

When the monthly requests are used up and no credits are left, calls are refused with `monthly_limit_reached` and a link to buy credits or upgrade. Over MCP, `get_usage` shows what is left.

Full error codes: [docs](https://www.trendsmcp.ai/docs.md). Do not commit keys. Claude.ai and ChatGPT connectors use OAuth; other clients use `Authorization: Bearer …`.

---

## What this does not do

- Related queries or related topics
- Hourly series (Google and YouTube go down to daily for the last 90 days)
- `get_time_series` across several sources in one call (use `get_growth` with a comma-separated `source` list, or several `get_time_series` calls)
- Inventing board names: `type` must match the table

---

## Develop this repo

```bash
pip install -e .
python -m trends_mcp_server
```

CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml). Security: [SECURITY.md](SECURITY.md). Issues: [github.com/trendsmcp-ai/Trends-MCP/issues](https://github.com/trendsmcp-ai/Trends-MCP/issues).

---

## Links

- [Account / key](https://www.trendsmcp.ai/account)
- [Docs](https://www.trendsmcp.ai/docs)
- [Pricing](https://www.trendsmcp.ai/pricing)
- [llms.txt](https://www.trendsmcp.ai/llms.txt)
- [TrendWatch](https://github.com/trendsmcp-ai/TrendWatch) (alerts in your own GitHub repo)

MIT © [Trends MCP](https://www.trendsmcp.ai)
