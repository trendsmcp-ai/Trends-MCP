---
title: "Reddit Discussion Volume Data for AI via MCP | Trends MCP"
description: "Structured Reddit discussion volume data for AI agents via MCP. Topic momentum, community growth signals, and historical series. No API rate limits."
canonical: "https://trendsmcp.ai/reddit-discussion-data"
---

# Reddit discussion volume data for AI agents

> Structured Reddit discussion data your AI can use to gauge community interest at scale. Find out which topics are gaining Reddit momentum, and whether that momentum is accelerating or cooling.

**Full page with live demo:** [https://trendsmcp.ai/reddit-discussion-data](https://trendsmcp.ai/reddit-discussion-data)

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
get_growth(keyword='decentralized finance', source='reddit', percent_growth=['6M'])
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

### What format does Reddit discussion data return?

JSON with normalized platform interest (0-100), growth percentage over the chosen period, and a weekly time series. Includes a data quality score indicating coverage reliability.

### Can I use Reddit data to validate a startup idea?

Yes. A common pattern is to check if community discussion around a problem or category is growing on Reddit, which can indicate increasing awareness and demand even before mainstream adoption.

### How often is the data updated?

Weekly data is refreshed weekly. Daily data (last 30 days) is updated daily. Results are cached for performance and refreshed automatically.

---

## Related

- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [google-search-data](https://trendsmcp.ai/google-search-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/reddit-discussion-data](https://trendsmcp.ai/reddit-discussion-data)*