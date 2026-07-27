<div align="center">

<img src="https://www.trendsmcp.ai/static/pages/trendsmcp/assets/trend.svg" width="72" alt="Trends MCP logo">

# Trends MCP

**Live trend data for your AI. 25+ platforms. One connection.**

Google Search · YouTube · TikTok · Reddit · Amazon · Wikipedia · X · News sentiment · App Store · npm · Steam · GitHub · Spotify · and more

[![MCP](https://img.shields.io/badge/MCP-compatible-blue)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Smithery](https://img.shields.io/badge/Smithery-listed-8A2BE2)](https://smithery.ai/servers/trendsmcp/trends-mcp)
[![API calls served](https://img.shields.io/badge/API%20calls%20served-4.1M%2B-brightgreen)](https://trendsmcp.ai)
[![Free tier](https://img.shields.io/badge/Free%20tier-100%20req%2Fmo-orange)](https://trendsmcp.ai?utm_source=github&utm_medium=readme&utm_campaign=badges)
[![GitHub stars](https://img.shields.io/github/stars/trendsmcp-ai/Trends-MCP?style=social)](https://github.com/trendsmcp-ai/Trends-MCP/stargazers)

[**Get a free API key →**](https://trendsmcp.ai?utm_source=github&utm_medium=readme&utm_campaign=hero) &nbsp;·&nbsp; [Docs](https://trendsmcp.ai/docs) &nbsp;·&nbsp; [Data Sources](https://trendsmcp.ai/data-sources) &nbsp;·&nbsp; [Use Cases](https://trendsmcp.ai/use-cases)

<img width="1841" alt="Trends MCP — live trend data across 25+ platforms" src="https://github.com/user-attachments/assets/e50e3025-cbdf-4f08-b0df-c1219e237f31" />

<!-- UPGRADE: replace the static screenshot above with a <20s demo GIF (convert the R2 .mov of
     Claude calling TrendsMCP). Animated hero > static hero for conversion. -->

</div>

---

## Why this exists

Your AI has a training cutoff. The world doesn't.

```
You: "Using TrendsMCP, compare 6-month growth for 'GLP-1' across Google, TikTok and Amazon."

Claude: GLP-1 momentum, last 6 months:
  Google Search  +84%  (accelerating)
  TikTok         +212% (breakout)
  Amazon         +61%  (steady)
```

One MCP endpoint replaces per-platform API keys, brittle scrapers (looking at you, pytrends), and $500/mo dashboard tools. Everything comes back as normalized 0–100 JSON your AI can reason over directly — ~5 years of weekly history per keyword.

| Problem | Trends MCP solution |
|---------|---------------------|
| AI has a training cutoff — it doesn't know what's trending today | Live data from 25+ sources, queried at request time |
| Separate keys and APIs for TikTok, Reddit, YouTube, Amazon… | One MCP endpoint, one key, consistent schema |
| pytrends scrapes Google and breaks constantly | Managed pipeline with retries, no scraping |
| Trend data comes back as charts you read manually | Structured JSON your AI reasons over directly |
| Expensive enterprise dashboards just for trend signals | Free tier, no dashboard, no per-seat pricing |

<img width="400" alt="Trends MCP in action" src="https://github.com/user-attachments/assets/6ff0e7ae-7f2d-460f-9a1c-5fd542d7fb77" />

## Quickstart (30 seconds)

**1.** Grab a free API key at [trendsmcp.ai](https://trendsmcp.ai?utm_source=github&utm_medium=readme&utm_campaign=quickstart) — 100 requests/mo, no credit card.

**2.** One-click install:

[<img src="https://cdn.simpleicons.org/claude/DA7756" width="14"> **Add to Claude**](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Trends%20MCP&connectorUrl=https%3A%2F%2Fwww.trendsmcp.ai%2Fmcp) &nbsp;·&nbsp; [**Add to Cursor**](cursor://anysphere.cursor-deeplink/mcp/install?name=trends-mcp&config=eyJ1cmwiOiJodHRwczovL2FwaS50cmVuZHNtY3AuYWkvbWNwIiwidHJhbnNwb3J0IjoiaHR0cCIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciBZT1VSX0FQSV9LRVkifX0%3D) &nbsp;·&nbsp; [**Smithery**](https://smithery.ai/servers/trendsmcp/trends-mcp)

Or paste the config:

<details open>
<summary><b>Cursor / Windsurf</b> - <code>~/.cursor/mcp.json</code></summary>

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
<summary><b>Cline</b> - see <code>llms-install.md</code> (requires <code>streamableHttp</code>)</summary>

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
<summary><b>VS Code / GitHub Copilot</b> — <code>.vscode/mcp.json</code></summary>

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
<summary><b>Claude Desktop</b> — <code>claude_desktop_config.json</code></summary>

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
<summary><b>Claude.ai (browser)</b> — Settings → Connectors → Add custom connector</summary>

```
https://www.trendsmcp.ai/mcp
```
</details>

**3.** Ask your AI:

```
Using TrendsMCP, what's trending on Google right now?
```

## The three tools

| Tool | What it does | Example |
|------|--------------|---------|
| `get_trends` | ~5 years of weekly history for a keyword, normalized 0–100 | `get_trends(keyword='electric vehicles', source='google search', data_mode='weekly')` |
| `get_growth` | % change over 7D–5Y, multi-source in one call | `get_growth(keyword='vibe coding', source='google search, tiktok, youtube', percent_growth=['3M','1Y'])` |
| `get_top_trends` | Live leaderboards — no keyword needed | `get_top_trends(type='TikTok Trending Hashtags', limit=20)` |

**Keyword sources** (`get_trends` / `get_growth`): `google search`, `google images`, `google news`, `google shopping`, `youtube`, `tiktok`, `reddit`, `amazon`, `wikipedia`, `news volume`, `news sentiment`, `app downloads`, `app rankings`, `npm`, `steam`

**Live feeds** (`get_top_trends`): Google Trends, Google News, TikTok Hashtags, YouTube, X (Twitter), Reddit Hot / World News, Wikipedia, Amazon Best Sellers, App Store Free/Paid, Google Play, Top Websites, Spotify Podcasts, Steam Most Played, GitHub Trending Repos, IMDb, Open Library → [full reference](https://trendsmcp.ai/docs#sources)

## Prompts that work

```
Is consumer interest in 'creatine gummies' growing or dying? Check Google, TikTok and Amazon.
```
```
Which npm packages in the MCP ecosystem are growing fastest right now?
```
```
Show news sentiment for 'Meta' over the past 6 months — is coverage turning positive?
```
```
Pull 5-year Google trend data for 'protein soda' and tell me if this is a fad or a durable shift.
```
```
What's on GitHub Trending today, and which repos relate to AI agents?
```

More recipes in [`examples/`](examples/) — market research, SEO, e-commerce demand validation, investor signal scans, content calendars.

## REST API (same key)

```python
import requests

r = requests.post(
    "https://api.trendsmcp.ai/api",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={"mode": "get_growth", "source": "google search",
          "keyword": "bitcoin", "percent_growth": ["3M", "12M"]},
)
print(r.json())
```

Full API reference: [trendsmcp.ai/docs](https://trendsmcp.ai/docs) · Errors are JSON with `error` + `message`; hitting your monthly cap returns `429 rate_limited` — no surprise overages.

## vs. the alternatives

| | Trends MCP | pytrends | Platform APIs | Exploding Topics / Glimpse |
|---|---|---|---|---|
| Live data in your AI via MCP | ✅ | ❌ | ❌ | ❌ |
| Sources per key | 25+ | 1 (scraped) | 1 each | dashboard only |
| Breaks when Google changes HTML | No | Constantly | — | — |
| Cross-platform normalized index | ✅ 0–100 | ❌ | ❌ | partial |
| Historical depth | ~5y weekly | varies | varies | paid tiers |
| Free tier | 100 req/mo | free until blocked | varies | trial |
| Setup time | 30 sec | pip + pray | days of OAuth | n/a |

## FAQ

<details><summary><b>Is the data normalized?</b></summary>
Yes — 0–100 index where the pipeline supports it, so search, social and commerce signals are directly comparable in one query. Proprietary estimates, not official platform figures.</details>

<details><summary><b>Which clients work?</b></summary>
Claude (Desktop, claude.ai, Code), Cursor, Windsurf, VS Code, GitHub Copilot, Cline, ChatGPT, Raycast, LangChain — anything MCP-compatible. <a href="https://trendsmcp.ai/docs">Per-client guides</a>.</details>

<details><summary><b>What does it cost?</b></summary>
Free forever: 100 req/mo. Starter $19/mo (1,000), Pro $49/mo (5,000), Business $199/mo (25,000). Annual −20%. <a href="https://trendsmcp.ai/pricing">Pricing</a>.</details>

<details><summary><b>Do I need per-platform API keys?</b></summary>
No. One Trends MCP key covers all sources — upstream access is handled for you. No scraping on your side.</details>

<details><summary><b>Setup guides per client</b></summary>

[Claude](https://trendsmcp.ai/mcp-server-for-claude) · [Cursor](https://trendsmcp.ai/mcp-server-for-cursor) · [VS Code](https://trendsmcp.ai/mcp-server-for-vs-code) · [Windsurf](https://trendsmcp.ai/mcp-server-for-windsurf) · [Copilot](https://trendsmcp.ai/mcp-server-for-github-copilot) · [Cline](https://trendsmcp.ai/mcp-server-for-cline) · [ChatGPT](https://trendsmcp.ai/mcp-server-for-chatgpt) · [Raycast](https://trendsmcp.ai/mcp-server-for-raycast) · [OpenAI](https://trendsmcp.ai/mcp-server-for-openai)
</details>

<details><summary><b>Data source deep-dives</b></summary>

[Google Trends](https://trendsmcp.ai/google-trends) · [YouTube](https://trendsmcp.ai/youtube-trends) · [TikTok](https://trendsmcp.ai/tiktok-trends) · [Reddit](https://trendsmcp.ai/reddit-trends) · [Amazon](https://trendsmcp.ai/amazon-search-trends) · [Wikipedia](https://trendsmcp.ai/wikipedia-trends) · [News sentiment](https://trendsmcp.ai/news-sentiment-data) · [Web traffic](https://trendsmcp.ai/web-traffic-data) · [App downloads](https://trendsmcp.ai/app-download-trends) · [Steam](https://trendsmcp.ai/steam-trends) · [npm](https://trendsmcp.ai/npm-trends) · [X/Twitter](https://trendsmcp.ai/twitter-trends) · [GitHub](https://trendsmcp.ai/github-trends) · [Spotify](https://trendsmcp.ai/spotify-trends) · [Google Shopping](https://trendsmcp.ai/google-shopping-trends) · [Google News](https://trendsmcp.ai/google-news-trends) · [Google Images](https://trendsmcp.ai/google-images-trends)
</details>

<details><summary><b>Use cases & alternatives</b></summary>

[Market research](https://trendsmcp.ai/market-research) · [Investment research](https://trendsmcp.ai/investment-research) · [Competitor tracking](https://trendsmcp.ai/competitor-tracking) · [Brand monitoring](https://trendsmcp.ai/brand-monitoring) · [SEO keyword research](https://trendsmcp.ai/seo-keyword-research) · [Content strategy](https://trendsmcp.ai/content-strategy) · [Social listening](https://trendsmcp.ai/social-listening-ai) · [E-commerce product research](https://trendsmcp.ai/ecommerce-product-research) · [Viral trend detection](https://trendsmcp.ai/viral-trend-detection) · [pytrends alternative](https://trendsmcp.ai/pytrends-alternative) · [Exploding Topics alternative](https://trendsmcp.ai/exploding-topics-alternative) · [Glimpse alternative](https://trendsmcp.ai/glimpse-alternative) · [Semrush alternative](https://trendsmcp.ai/semrush-alternative) · [SimilarWeb alternative](https://trendsmcp.ai/similarweb-alternative)
</details>

## Ecosystem

- **[TrendWatch](https://github.com/trendsmcp/TrendWatch)** — free trend-monitoring bot that runs in your own GitHub repo. Slack/Discord/Telegram/email alerts when a keyword spikes. No server needed.
- Single-source MCP servers: [google-search-trends-mcp](https://github.com/trendsmcp/google-search-trends-mcp) · [tiktok-trends-mcp](https://github.com/trendsmcp/tiktok-trends-mcp) · [reddit-trends-mcp](https://github.com/trendsmcp/reddit-trends-mcp) · [news-sentiment-mcp](https://github.com/trendsmcp/news-sentiment-mcp) · [steam-trends-mcp](https://github.com/trendsmcp/steam-trends-mcp) · [more →](https://github.com/trendsmcp?tab=repositories)

---

<div align="center">

**If Trends MCP saves you from writing another scraper, [give it a ⭐](https://github.com/trendsmcp/Trends-MCP) — it genuinely helps.**

[**Get your free API key →**](https://trendsmcp.ai?utm_source=github&utm_medium=readme&utm_campaign=footer)

MIT © [Trends MCP](https://trendsmcp.ai)

</div>
