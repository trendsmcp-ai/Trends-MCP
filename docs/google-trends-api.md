---
title: "Google Trends API for AI Agents - MCP Alternative | Trends MCP"
description: "The practical Google Trends API for AI assistants. Get absolute search volume, multi-source comparison, and 5-year history via MCP. No scraping, no quota limits."
canonical: "https://trendsmcp.ai/google-trends-api"
---

# Google Trends API for AI agents

> The official Google Trends site has no public API. Trends MCP fills that gap: structured Google Search trend data delivered to any AI assistant via the Model Context Protocol. Absolute volume estimates, multi-source comparison, 5-year history -- all in one clean JSON response.

**Full page with live demo:** [https://trendsmcp.ai/google-trends-api](https://trendsmcp.ai/google-trends-api)

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
get_growth(keyword='model context protocol', source='google search', percent_growth=['3M', '1Y'])
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

### Does Google have an official Trends API?

No. Google Trends has no official public API. The website provides relative interest data with no programmatic access. Trends MCP provides a structured, AI-native alternative that returns absolute volume estimates, growth metrics, and historical time series via the Model Context Protocol.

### How does Trends MCP differ from pytrends?

pytrends is a Python library that scrapes the Google Trends website, returns only relative (0-100) interest scores, and is subject to rate limiting and breakage when Google changes its frontend. Trends MCP returns absolute volume estimates, supports multi-source queries across 12+ platforms in one call, and is designed for AI agents rather than Python scripts.

### Can I get absolute Google Search volume, not just relative interest?

Yes. Trends MCP adds absolute query volume estimates alongside the normalized 0-100 signal. These are directionally accurate for trend analysis -- suitable for comparing keyword momentum, not for ad campaign budgeting.

### What does the JSON response look like?

A structured object with: keyword, source, normalized_value (0-100), absolute_volume_estimate, growth_pct (per period), time_series (array of date/value pairs), and data_quality_score.

### Is there a rate limit?

Trends MCP operates within your plan's query limits. Unlike scraping pytrends, there are no IP-based rate limits or Google bot-detection issues to manage.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [pytrends-alternative](https://trendsmcp.ai/pytrends-alternative)
- [google-trends-alternative](https://trendsmcp.ai/google-trends-alternative)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-trends-api](https://trendsmcp.ai/google-trends-api)*