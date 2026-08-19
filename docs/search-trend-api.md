---
title: "Search Trend API for Developers - MCP-Native Trend Data | Trends MCP"
description: "Search trend API built for developers and AI agents. Get structured search volume, trend history, and growth metrics from Google, YouTube, Amazon, and more via MCP."
canonical: "https://trendsmcp.ai/search-trend-api"
---

# Search trend API for developers

> A search trend API designed from the ground up for AI agents and developers. Unlike fragile web scrapers or Google's unofficial pytrends library, Trends MCP provides a stable, normalized, MCP-native interface to search trend data across Google, YouTube, Amazon, and 9 more sources.

**Full page with live demo:** [https://trendsmcp.ai/search-trend-api](https://trendsmcp.ai/search-trend-api)

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
get_trends(keyword='next.js', source='google search', data_mode='weekly')
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

### What does the search trend API return?

For each query: normalized interest values (0-100), absolute volume estimates, week-by-week or month-by-month time series, growth percentages, and data quality scores. All returned as structured JSON compatible with any AI agent tool-calling interface.

### Is it MCP-native or a REST API?

Trends MCP is delivered as a Model Context Protocol server, which means AI agents connect to it directly using the MCP standard. For direct REST access, the underlying API endpoint is also available at api.trendsmcp.ai.

### How reliable is the data compared to pytrends?

pytrends scrapes the Google Trends website and breaks whenever Google changes its frontend. Trends MCP uses a managed data pipeline with built-in retries, rate-limit handling, and fallback sources. It is designed for production AI agent use, not one-off scripts.

### Can I use this for programmatic SEO content generation?

Yes. Many teams use Trends MCP to feed their AI writing workflows with live keyword trend data -- identifying growing topics before writing about them and validating content angles with real search momentum data.

---

## Related

- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)
- [pytrends-alternative](https://trendsmcp.ai/pytrends-alternative)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/search-trend-api](https://trendsmcp.ai/search-trend-api)*