---
title: "Keyword Trend Data for AI - Live Search Volume via MCP | Trends MCP"
description: "Live keyword trend data for AI assistants and SEO tools. Get search volume history, growth rates, and cross-platform keyword momentum via MCP. No scraping."
canonical: "https://trendsmcp.ai/keyword-trend-data"
---

# Keyword trend data for AI assistants

> Ask your AI whether a keyword is growing or declining -- and get the answer from 12 sources simultaneously. Trends MCP delivers keyword search volume history, growth rates, and cross-platform momentum signals structured for AI agents. Google, YouTube, Reddit, TikTok, Amazon, and more in one call.

**Full page with live demo:** [https://trendsmcp.ai/keyword-trend-data](https://trendsmcp.ai/keyword-trend-data)

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
get_growth(keyword='electric vehicles', source='google search, youtube, reddit', percent_growth=['3M', '1Y'])
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

### What keyword trend data does Trends MCP provide?

For any keyword: normalized interest score (0-100), absolute volume estimate, 5-year historical time series, growth percentage over multiple periods (1 week, 1 month, 3 months, 1 year), and cross-platform comparison across up to 12 sources.

### How is this different from a standard keyword research tool?

Standard keyword tools (Ahrefs, SEMrush, etc.) show search volume for SEO planning. Trends MCP shows trend velocity -- whether interest is growing, stable, or declining -- across search, social, video, and commerce simultaneously. It is designed for real-time research, not ad campaign keyword lists.

### Can I track keyword trends across multiple platforms at once?

Yes. Use get_growth with source='all' to compare a keyword's momentum across all available platforms in a single query. You will see whether the same keyword is growing on Google but declining on TikTok, for example.

### Is keyword data available for specific countries?

Yes. Most sources support geographic filtering. Pass the region parameter to get country-specific or city-specific keyword trend data.

---

## Related

- [seo-keyword-research](https://trendsmcp.ai/seo-keyword-research)
- [google-trends](https://trendsmcp.ai/google-trends)
- [real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/keyword-trend-data](https://trendsmcp.ai/keyword-trend-data)*