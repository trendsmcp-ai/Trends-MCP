---
title: "Google Shopping Trends MCP - Product Search Data for AI | Trends MCP"
description: "Query Google Shopping search trends from any AI via MCP. Track product purchase intent, rising categories, and historical shopping search volume. No API key."
canonical: "https://trendsmcp.ai/google-shopping-trends"
---

# Google Shopping trend data for AI assistants

> Google Shopping search signals reveal active product purchase intent. When people search on Google Shopping, they are ready to buy. Track which product categories and keywords are driving purchase intent right now.

**Full page with live demo:** [https://trendsmcp.ai/google-shopping-trends](https://trendsmcp.ai/google-shopping-trends)

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
get_trends(keyword='standing desk', source='google shopping', data_mode='weekly')
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

### What is Google Shopping trend data?

Shopping search volume trends reflecting how often people search for products on Google Shopping specifically - a higher purchase-intent signal than general Google Search.

### How is Google Shopping data different from Amazon search data?

Google Shopping reflects cross-retailer purchase intent (people comparing products across many retailers). Amazon reflects intent to buy specifically on Amazon. Together they give a complete picture of consumer purchase demand.

### Is this useful for retail and e-commerce research?

Yes. Track which product keywords are growing on Google Shopping to identify demand shifts before they show up in sales data. Particularly useful for seasonal planning and new product category research.

---

## Related

- [amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)
- [google-search-data](https://trendsmcp.ai/google-search-data)
- [amazon-product-data](https://trendsmcp.ai/amazon-product-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-shopping-trends](https://trendsmcp.ai/google-shopping-trends)*