---
title: "Web Traffic Data for AI via MCP | Trends MCP"
description: "Query website traffic trend data from any AI assistant via MCP. Track site visit trends, domain growth, and competitive traffic signals via SimilarWeb."
canonical: "https://trendsmcp.ai/web-traffic-data"
---

# Web traffic trend data for AI assistants

> Track website visit trends for any domain or company. Measure audience growth, detect traffic spikes from product launches or press coverage, and compare competitors side by side - all from your AI.

**Full page with live demo:** [https://trendsmcp.ai/web-traffic-data](https://trendsmcp.ai/web-traffic-data)

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
get_trends(keyword='shopify.com', source='webtraffic', data_mode='weekly')
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

### What web traffic data does Trends MCP provide?

Normalized website visit trend data sourced from SimilarWeb estimates. Returns monthly traffic trends, growth rates, and historical time series for any domain.

### Can I compare multiple domains at once?

Yes. Pass a list of domains and get comparative traffic growth metrics back in a structured response - useful for competitive benchmarking.

### How accurate are the traffic estimates?

Traffic estimates are sourced from SimilarWeb panel data and are directionally accurate for medium-to-large sites. Small sites with under ~50K monthly visits may have lower data quality scores.

### Can I query a company name instead of a domain?

Yes. The system resolves common company names to their primary domain automatically.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [website-traffic-trends](https://trendsmcp.ai/website-traffic-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/web-traffic-data](https://trendsmcp.ai/web-traffic-data)*