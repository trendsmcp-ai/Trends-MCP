---
title: "Trending Topics API for AI - Live Trending Data via MCP | Trends MCP"
description: "Get trending topics from Google, TikTok, Reddit, YouTube, and more via a single API for AI assistants. Real-time trending keywords, hashtags, and discussions via MCP."
canonical: "https://trendsmcp.ai/trending-topics-api"
---

# Trending topics API for AI assistants

> What is trending right now on Google? On TikTok? On Reddit? Trends MCP gives your AI a single API call to answer all three -- and nine more sources. Get real-time trending topics, breakout keywords, and rising discussions delivered as structured data your AI can immediately act on.

**Full page with live demo:** [https://trendsmcp.ai/trending-topics-api](https://trendsmcp.ai/trending-topics-api)

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
get_top_trends(source='all', limit=10)
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

### What sources does the trending topics API cover?

Google Search, TikTok hashtags, Reddit discussions, YouTube videos, Amazon products, Wikipedia articles, News stories, and more -- 12+ sources in total. Each returns the current top trending items with volume and growth signals.

### How does trending topics data differ from keyword search volume?

Search volume is historical and slow-moving. Trending topics captures what is spiking right now -- breakout queries that are growing 100%+ week-over-week. Trends MCP provides both: use get_top_trends for what is trending now and get_growth for measuring momentum over time.

### Can I filter trending topics by category?

Yes. Many sources support category filtering. You can request trending topics within specific categories like technology, finance, entertainment, or sports depending on the platform.

### How do I integrate this into an AI agent workflow?

Connect Trends MCP to your AI client (Claude, ChatGPT, Cursor, etc.) and ask it to call get_top_trends. The agent receives a ranked list of trending topics with volume and growth data it can use for reporting, content planning, or further research.

---

## Related

- [real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)
- [google-trends](https://trendsmcp.ai/google-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/trending-topics-api](https://trendsmcp.ai/trending-topics-api)*