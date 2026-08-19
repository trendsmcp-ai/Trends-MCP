---
title: "Google Trends Data for AI - Structured Search Data via MCP | Trends MCP"
description: "Get structured Google Trends data in your AI assistant via MCP. Search volume, growth rates, breakout topics, and 5-year history. No scraping, no quota limits."
canonical: "https://trendsmcp.ai/google-trends-data"
---

# Google Trends data for AI

> Google Trends data is valuable but hard to use programmatically. Trends MCP solves that: structured, normalized Google Search trend data delivered to any AI assistant via MCP. Ask your AI about search momentum, breakout keywords, or 5-year trends for any topic -- and get clean, reasoned answers.

**Full page with live demo:** [https://trendsmcp.ai/google-trends-data](https://trendsmcp.ai/google-trends-data)

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
get_trends(keyword='climate change', source='google search', data_mode='monthly')
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

### What Google Trends data can I access?

Search interest over time (normalized 0-100 and absolute volume estimates), breakout keywords and rising queries, top trending topics by category, geographic breakdown, and 5-year historical time series. All available via simple MCP tool calls.

### How is this different from visiting Google Trends directly?

Google Trends is a web interface for manual browsing. Trends MCP delivers the same data as structured JSON to your AI assistant, so the AI can analyze, compare, and reason over it directly -- no manual chart reading or CSV exporting required.

### Can I get absolute search volume, not just relative interest?

Yes. Trends MCP adds absolute volume estimates alongside the standard 0-100 normalized score. These are suitable for trend comparison and momentum analysis.

### Does the data include related queries and rising topics?

Yes. The get_top_trends tool returns the current top trending searches and breakout topics on Google, updated in near-real-time.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [keyword-trend-data](https://trendsmcp.ai/keyword-trend-data)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-trends-data](https://trendsmcp.ai/google-trends-data)*