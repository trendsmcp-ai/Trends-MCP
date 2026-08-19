---
title: "Google Search Data API for AI via MCP | Trends MCP"
description: "Access structured Google Search demand data in AI assistants via MCP. Raw query volume, normalized signals, and historical series. No Google API key needed."
canonical: "https://trendsmcp.ai/google-search-data"
---

# Google Search demand data for AI agents

> Raw, structured Google Search demand data delivered directly to your AI. No API keys, no quotas, no scraping. Just query a keyword and get normalized volume, historical series, and growth signals back in seconds.

**Full page with live demo:** [https://trendsmcp.ai/google-search-data](https://trendsmcp.ai/google-search-data)

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
get_trends(keyword='cloud security', source='google search', data_mode='weekly')
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

### What format does Google Search data come back in?

JSON with a time series array (date + normalized value + absolute volume), a summary object with growth metrics, and a data quality score indicating coverage reliability.

### Do I need a Google API key to use this?

No. Trends MCP handles all source connectivity. You connect once via the MCP config snippet and your AI can query Google Search data immediately.

### How accurate is the absolute volume estimate?

Volume estimates are derived from normalized Google Trends data combined with third-party search volume calibration. They are directionally accurate for trend analysis but should not be treated as exact query counts.

### Can AI agents use this data for market research?

Yes. A common pattern is: query a set of product or company keywords, rank them by search demand growth, and identify which has the strongest consumer interest signal.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [google-search-trends](https://trendsmcp.ai/google-search-trends)
- [amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-search-data](https://trendsmcp.ai/google-search-data)*