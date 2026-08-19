---
title: "Amazon Product Search Data for AI via MCP | Trends MCP"
description: "Structured Amazon product search volume data for AI agents via MCP. Consumer demand trends, growth metrics, and historical series. No Amazon Seller account needed."
canonical: "https://trendsmcp.ai/amazon-product-data"
---

# Amazon product search volume data for AI agents

> Structured consumer purchase-intent data from Amazon, delivered directly to your AI. Identify growing product categories, measure demand seasonality, and track competitor keyword momentum without an Amazon Seller account.

**Full page with live demo:** [https://trendsmcp.ai/amazon-product-data](https://trendsmcp.ai/amazon-product-data)

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
get_growth(keyword='collagen supplements', source='amazon', percent_growth=['1Y', '3M'])
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

### What does Amazon product data return?

JSON with normalized search volume (0-100), absolute volume estimate, growth percentage over the selected period, and a weekly time series array.

### Do I need an Amazon Seller Central account?

No. Trends MCP accesses Amazon search signals through normalized trend data, not the Amazon Advertising API. No seller account or API key is needed.

### Can this detect seasonal demand patterns?

Yes. The 5-year weekly time series clearly shows seasonal spikes - for example, gifting categories peaking in November-December or summer products peaking in May-June.

---

## Related

- [amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)
- [google-search-data](https://trendsmcp.ai/google-search-data)
- [google-shopping-trends](https://trendsmcp.ai/google-shopping-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/amazon-product-data](https://trendsmcp.ai/amazon-product-data)*