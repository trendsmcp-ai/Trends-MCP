---
title: "Real-Time Trends API for AI Agents - Live Data via MCP | Trends MCP"
description: "Real-time trends API for AI agents and assistants. Get live search volume, hashtag growth, and social trends from 12+ sources via MCP. No scraping, no API key juggling."
canonical: "https://trendsmcp.ai/real-time-trends-api"
---

# Real-time trends API for AI agents

> Most trend APIs return yesterday's data. Trends MCP delivers live, real-time trend signals from Google Search, TikTok, Reddit, YouTube, Amazon, and 8 more platforms -- structured for AI agents via the Model Context Protocol. One endpoint. No polling. No scraping.

**Full page with live demo:** [https://trendsmcp.ai/real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)

---

## Get started in 2 steps

**Step 1:** Get your free API key at **[trendsmcp.ai](https://trendsmcp.ai)**
100 requests/month, no credit card required.

**Step 2:** Add to your AI client (replace `YOUR_API_KEY`):

[**+ Add to Cursor (one click)**](cursor://anysphere.cursor-deeplink/mcp/install?name=trends-mcp&config=eyJ1cmwiOiJodHRwczovL2FwaS50cmVuZHNtY3AuYWkvdjEvbWNwIiwidHJhbnNwb3J0IjoiaHR0cCJ9)

**Cursor / Windsurf / Cline**
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

**VS Code / GitHub Copilot**
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

**Claude Desktop** &nbsp; add to `mcpServers`:
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

**Claude.ai** (browser) &nbsp; Settings → Connectors → Add custom connector:
```
https://api.trendsmcp.ai/mcp
```

---

## Example query

```
get_top_trends(source='google search', limit=20)
```

---

## What you get

- **12+ live data sources**: Google Search, YouTube, TikTok, Reddit, Amazon,
  Wikipedia, News sentiment, Web Traffic, App Downloads, Steam, npm, and more
- **Normalized 0-100 scale** across all platforms -- compare Google vs TikTok in one call
- **Absolute volume estimates** alongside relative interest scores
- **5-year historical time series** for any keyword
- **Growth %** over 1W, 1M, 3M, 1Y periods
- **One free API key** covers all 12+ sources -- no per-platform keys needed
- Works with **Claude, Cursor, VS Code, GitHub Copilot, ChatGPT, Windsurf, Cline, Raycast**

---

## FAQ

### How real-time is the trend data?

Data freshness varies by source. Google Trends data refreshes within hours. TikTok and Reddit trend data is near-live (minutes to hours). Wikipedia and news sources update continuously. All sources are queried at request time -- there is no stale cache served to your AI.

### What makes this different from other trend APIs?

Most trend APIs provide a single data source with rate limits, API key management, and inconsistent schemas. Trends MCP delivers 12+ normalized sources through a single MCP endpoint, designed specifically for AI agents. Your AI gets a structured JSON response it can reason over immediately.

### Do I need separate API keys for each platform?

No. Trends MCP manages all source access. You connect your AI to one endpoint and get all 12+ sources in every query session.

### What query tools are available?

get_trends (time-series for a keyword), get_growth (cross-source growth comparison), get_top_trends (what is trending now), and get_ranked_trends (top trends with volume ranking).

---

## Related

- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [trending-topics-api](https://trendsmcp.ai/trending-topics-api)
- [search-trend-api](https://trendsmcp.ai/search-trend-api)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)*