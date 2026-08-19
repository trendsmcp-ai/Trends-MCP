---
title: "AI E-commerce Product Research with Trend Data via MCP | Trends MCP"
description: "Find winning products with live trend data via MCP. Query Amazon, Google Shopping, TikTok, and Google Search demand signals from your AI. No manual lookups."
canonical: "https://trendsmcp.ai/ecommerce-product-research"
---

# AI-powered e-commerce product research with live demand data

> Find products with growing demand before everyone else does. Trends MCP gives your AI live Amazon search volume, Google Shopping purchase intent, TikTok viral signals, and Google Search interest -- the four signals that predict whether a product category is worth entering.

**Full page with live demo:** [https://trendsmcp.ai/ecommerce-product-research](https://trendsmcp.ai/ecommerce-product-research)

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
get_growth(keyword='mushroom coffee', source='amazon, google shopping, tiktok, google search', percent_growth=['1M', '3M', '1Y'])
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

### Which data sources matter most for e-commerce product research?

Amazon search volume (highest-intent purchase signal -- people on Amazon are ready to buy), Google Shopping (cross-retailer purchase intent), TikTok (viral demand that often predicts Amazon sales spikes 2-4 weeks ahead), and Google Search (broad consumer awareness). Together these four give a complete demand picture from awareness to purchase.

### Can Trends MCP help with dropshipping product research?

Yes. Query a list of product ideas across Amazon and TikTok. Products with rapidly growing TikTok hashtag volume but still-moderate Amazon search volume are early-stage opportunities -- high viral interest has not yet translated to saturated supply on Amazon.

### How far back does the product demand data go?

Up to 5 years of weekly data. This lets you distinguish genuine long-term trends from seasonal spikes or short-lived fads -- essential for deciding whether to build a product business around a category.

### Can I validate a product idea in one AI session?

Yes. A complete validation workflow: (1) Amazon demand growth, (2) Google Shopping purchase intent, (3) TikTok viral momentum, (4) Reddit community discussion, (5) 5-year Google Search trajectory. Your AI runs all five queries and synthesizes the results in one session.

---

## Related

- [market-research](https://trendsmcp.ai/market-research)
- [amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)
- [google-shopping-trends](https://trendsmcp.ai/google-shopping-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/ecommerce-product-research](https://trendsmcp.ai/ecommerce-product-research)*