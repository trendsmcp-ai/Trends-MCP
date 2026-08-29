<div align="center">

<!-- mcp-name: ai.trendsmcp/trends -->

<img src="https://www.trendsmcp.ai/static/pages/trendsmcp/assets/trend.svg" width="72" alt="Trends MCP logo">

# Trends MCP

Live trend data for AI agents. Google, TikTok, YouTube, Amazon, Reddit, and 30+ other sources. One MCP connection, one API key.

[![PyPI](https://img.shields.io/pypi/v/trends-mcp-server)](https://pypi.org/project/trends-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/trendsmcp-ai/Trends-MCP/actions/workflows/ci.yml/badge.svg)](https://github.com/trendsmcp-ai/Trends-MCP/actions/workflows/ci.yml)
[![MCP](https://img.shields.io/badge/MCP-remote%20%2B%20stdio-blue)](https://modelcontextprotocol.io)
[![Free tier](https://img.shields.io/badge/Free-100%20req%2Fmo-orange)](https://www.trendsmcp.ai/pricing)
[![Glama](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP/badges/score.svg)](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP)

[Get a free API key](https://www.trendsmcp.ai/account) · [Docs](https://www.trendsmcp.ai/docs) · [Pricing](https://www.trendsmcp.ai/pricing) · [Data sources](https://www.trendsmcp.ai/data-sources) · [PyPI](https://pypi.org/project/trends-mcp-server/) · [Glama](https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP)

<a href="https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP">
  <img width="380" src="https://glama.ai/mcp/servers/trendsmcp-ai/Trends-MCP/badges/card.svg" alt="Trends MCP on Glama">
</a>

</div>

```
You: Using TrendsMCP, compare 6-month growth for GLP-1 on Google, TikTok, and Amazon.

Agent: Google Search  +84%
       TikTok         +212%
       Amazon         +61%
```

Three tools. Normalized 0–100 where the pipeline supports it. No per-platform keys. No scraping on your side.

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
| **ChatGPT** | Enable Developer mode (Profile → Settings → Security). Name `Trends MCP`, URL `https://www.trendsmcp.ai/mcp`, then authorize. |
| **VS Code** | Sign in on the account page and use the **VS Code** button so the key is included. |

Then ask: `Using TrendsMCP, what's trending on Google right now?`

**[Tools](#tools)** · **[Sources](#keyword-sources)** · **[Feeds](#live-feeds)** · **[REST](#rest-api)** · **[Install in other clients](#install-in-other-clients)**

---

## What this is

Hosted MCP at `https://api.trendsmcp.ai/mcp`. Same Bearer key for `POST https://api.trendsmcp.ai/api`. This repo also has a stdio adapter for Glama and local hosts.

| Tool | Use when | Needs a keyword? |
|---|---|---|
| `get_time_series` | History for one keyword on one source | Yes |
| `get_growth` | Percent change over 7D–5Y (several windows in one call) | Yes |
| `get_top_trends` | What is ranking on a platform right now | No |

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

Hosted HTTP is still the product default. This process lists tools with no key; paid calls need `TRENDSMCP_API_KEY` and bill the same quota.

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

Always-current parameter lists: [docs](https://www.trendsmcp.ai/docs).

### `get_time_series`

Weekly (or daily) history for **one** `source` + `keyword`. Same name on MCP and REST (`mode: "get_time_series"`). REST also accepts `get_trends` as an alias.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | Format depends on source (table below) |
| `source` | yes | One source per call. Lowercase catalog names |
| `data_mode` | no | REST only. `weekly` (default) or `daily` |

Index is 0–100 where the pipeline supports it (100 = peak in the returned window). `volume` is present when that source has an absolute series.

### `get_growth`

Point-to-point percent change. Several windows in one call still count as **one** request for that source + keyword.

| Argument | Required | Notes |
|---|---|---|
| `keyword` | yes | Same formats as `get_time_series` |
| `source` | yes | One source, or a comma-separated list (`google search, tiktok, amazon`) |
| `percent_growth` | no | Default `["12M"]`. Presets below, or `{ "recent", "baseline", "name" }` date objects |

Presets: `7D` `14D` `30D` `1M` `2M` `3M` `6M` `9M` `12M` `1Y` `18M` `24M` `2Y` `36M` `3Y` `48M` `60M` `5Y` `MTD` `QTD` `YTD`.

### `get_top_trends`

Live ranked list. **No keyword.** On MCP, `type` is required and must match the feed name **exactly** (including capitals). On REST, omit `type` only if you intend to pull every feed (billed per feed).

| Argument | Required on MCP | Notes |
|---|---|---|
| `type` | yes | See [live feeds](#live-feeds) |
| `limit` | no | Default 25, max 200 |
| `offset` | no | Pagination |
| `category` | for some types | Amazon / Google Trends / Top Websites / Substack / TikTok hashtag category boards |
| `sort` | no | `rank` (default) or `rank_change` |
| `window` | no | With `sort=rank_change`: `1d` `3d` `7d` `14d` `30d` |

---

## Prompts that route correctly

```
Using TrendsMCP, what's trending on Google right now?
Using TrendsMCP, what are the hottest Reddit posts right now?
Using TrendsMCP, compare 6-month growth for creatine gummies on Google, TikTok, and Amazon.
Using TrendsMCP, show Google Search history for protein soda.
Via TrendsMCP, pull npm download history for langchain.
Using TrendsMCP, show Steam concurrent players for Elden Ring.
Via TrendsMCP, Android downloads for com.openai.chatgpt.
Using TrendsMCP, fastest-climbing Amazon best sellers in Toys Games this week.
```

---

## Keyword sources

`source` on `get_time_series` / `get_growth`. Not the same strings as `type` on live feeds.

| `source` | Signal | `keyword` |
|---|---|---|
| `google search` | Search volume | Any phrase |
| `google images` | Image search volume | Any phrase |
| `google news` | News-tab volume | Any phrase |
| `google shopping` | Shopping-tab volume | Any phrase |
| `youtube` | YouTube search volume | Any phrase |
| `tiktok` | Hashtag volume | Hashtag or topic (`#` optional) |
| `reddit` | Subreddit attention | Name only, no `r/` |
| `amazon` | Product search volume | Product or category |
| `wikipedia` | Page views | Article title or topic |
| `news volume` | Mention volume | Any phrase |
| `news sentiment` | News tone | Any phrase |
| `app downloads` | Android downloads | Play bundle id, e.g. `com.openai.chatgpt` |
| `app rankings` | Android chart position | Bundle id |
| `npm` | Weekly downloads | Exact package name (`react`, `@babel/core`) |
| `steam` | Monthly concurrent players | Game display name (`Elden Ring`) |

`source: "Google Trends"` is invalid. Use `google search` for history and `type: "Google Trends"` for the live board.

---

## Live feeds

`type` on `get_top_trends`. Copy the name exactly.

| `type` | Board |
|---|---|
| `Google Trends` | Google searches now |
| `Google Trends by Category` | Needs `category` (e.g. `Games`) |
| `Google News Top News` | Google News stories |
| `TikTok Trending Hashtags` | Hashtags |
| `TikTok Trending Hashtags by Category` | Needs `category` |
| `TikTok Trending Searches` | In-app searches |
| `YouTube Trending` | Videos |
| `X (Twitter) Trending` | Topics on X |
| `Reddit Hot Posts` | Front page |
| `Reddit World News` | r/worldnews |
| `Wikipedia Trending` | Most-viewed articles |
| `Amazon Best Sellers Top Rated` | Top-rated sellers |
| `Amazon Best Sellers by Category` | Needs `category` (e.g. `Toys Games`) |
| `App Store Top Free` / `App Store Top Paid` | iOS charts |
| `Google Play` | Play chart |
| `Top Websites` | Global traffic rank; optional `category` |
| `Spotify Top Podcasts` | Podcasts |
| `Steam Most Played` | Live players |
| `Substack` / `Substack by Category` | Newsletters |
| `GitHub` | Daily trending repos |
| `IMDb MOVIEmeter` | Movie activity |
| `Open Library Trending Books` | Books |

Category name lists: [docs](https://www.trendsmcp.ai/docs).

iOS charts, GitHub repos, Spotify, IMDb, Open Library, Substack, and Top Websites are **feeds**, not `source` values. There is no `source: "web traffic"`.

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

| Plan | Requests / month | Price |
|---|---|---|
| Free | 100 | $0 |
| Starter | 1,000 | $19 |
| Pro | 5,000 | $49 |
| Business | 25,000 | $199 |

Annual billing is 20% less. Same source catalog on every plan. Free history and “top N” caps are on [pricing](https://www.trendsmcp.ai/pricing). Failed calls are not billed. Over quota returns `429` / `rate_limited` (no surprise overages).

One billed request:

- `get_time_series`: one source + keyword
- `get_growth`: one source + keyword (all windows in that call included)
- `get_top_trends`: per `type` (and pagination as documented)

| Status | Meaning |
|---|---|
| 400 | Bad or missing `source` / `type` / field |
| 401 | Missing or invalid key |
| 404 | No series for that keyword + source |
| 429 | Monthly cap |
| 500 | Upstream or internal error |

Do not commit keys. Claude.ai connectors use OAuth; other clients use `Authorization: Bearer …`.

---

## What this does not do

- Region / geo breakdown, related queries, or related topics
- Hourly series
- `get_time_series` across several sources in one call (use `get_growth` with a comma-separated `source` list, or several `get_time_series` calls)
- Inventing feed names: MCP `type` must match the table

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
- [TrendWatch](https://github.com/trendsmcp/TrendWatch) (alerts in your own GitHub repo)

MIT © [Trends MCP](https://www.trendsmcp.ai)
