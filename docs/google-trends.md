---
title: "Google Trends MCP Server - Live Data for AI Assistants | Trends MCP"
description: "Query live Google Trends data from any AI assistant via MCP. Get real-time trending topics, breakout keywords, and 5-year search interest history. Instant setup."
canonical: "https://trendsmcp.ai/google-trends"
---

# Google Trends data for AI assistants

> Ask your AI what is trending on Google right now. Get breakout keywords, rising topics, and 5 years of normalized search interest data - without writing a single line of scraping code.

**Full page with live demo:** [https://trendsmcp.ai/google-trends](https://trendsmcp.ai/google-trends)

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
get_trends(keyword='artificial intelligence', source='google search', data_mode='weekly')
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

### What Google Trends data does Trends MCP return?

Trends MCP returns normalized search interest (0-100 scale), absolute search volume estimates, weekly or daily time series, and growth rate over your chosen period. Data reflects real Google Search demand.

### How is this different from the official Google Trends website?

Google Trends shows relative interest only. Trends MCP adds absolute volume estimates, structured JSON output your AI can reason over, and cross-platform comparison - so you can compare Google interest against TikTok or Reddit in one query.

### Can I get Google Trends data for multiple keywords at once?

Yes. Pass a list of keywords and the MCP server returns normalized series for each, aligned on the same timeline so your AI can compare them directly.

### How far back does Google Trends data go?

Up to 5 years of weekly data or 30 days of daily data. Use the period parameter: '5y', '1y', '3m', '1m', or '30d'.

### Does it support geographic filtering?

Yes. You can filter by country code (e.g. US, GB, DE) to get region-specific search interest instead of global data.

---

## Related

- [google-search-trends](https://trendsmcp.ai/google-search-trends)
- [google-search-data](https://trendsmcp.ai/google-search-data)
- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-trends](https://trendsmcp.ai/google-trends)*