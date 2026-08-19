---
title: "Amazon Search Trends MCP - Product Demand Data for AI | Trends MCP"
description: "Query Amazon product search volume trends from any AI via MCP. Track consumer product demand, rising categories, and historical search interest. No Amazon API."
canonical: "https://trendsmcp.ai/amazon-search-trends"
---

# Amazon search trend data for AI assistants

> Measure real consumer purchase intent. Amazon search volume reveals what people are actively looking to buy - not just research. Historical demand curves and growth signals, queryable by your AI.

**Full page with live demo:** [https://trendsmcp.ai/amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)

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
get_trends(keyword='air fryer', source='amazon', data_mode='weekly')
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

### What Amazon data does Trends MCP provide?

Amazon product search volume trends - normalized interest over time reflecting consumer purchase intent. This is distinct from Google Search data because Amazon queries represent active buying intent rather than general information seeking.

### Is Amazon search data useful for e-commerce product research?

Yes. Compare product keyword demand on Amazon vs. Google to understand whether consumer intent is primarily informational or transactional. Rising Amazon search is a strong buying signal.

### Can I track a whole product category?

Yes. Use a category keyword like 'bluetooth headphones' or 'protein powder' and the signal aggregates demand across that category on Amazon.

### How is Amazon trend data normalized?

All values are normalized to a 0-100 scale for consistent comparison. An absolute volume estimate is also returned alongside the normalized signal.

---

## Related

- [google-search-data](https://trendsmcp.ai/google-search-data)
- [google-trends](https://trendsmcp.ai/google-trends)
- [amazon-product-data](https://trendsmcp.ai/amazon-product-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)*