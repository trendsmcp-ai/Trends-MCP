---
title: "Website Traffic Trends via MCP - Domain Data for AI | Trends MCP"
description: "Track website traffic trends for any domain from your AI via MCP. Growth rates, visit history, and competitive benchmarks. Powered by SimilarWeb estimates."
canonical: "https://trendsmcp.ai/website-traffic-trends"
---

# Website traffic growth trends for AI agents

> Measure how website traffic is growing or declining for any domain. Competitive benchmarking, traffic spike attribution, and long-term audience growth signals - structured for AI analysis.

**Full page with live demo:** [https://trendsmcp.ai/website-traffic-trends](https://trendsmcp.ai/website-traffic-trends)

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
get_growth(keyword='notion.so', source='webtraffic', percent_growth=['1Y', '6M'])
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

### What is the difference between web traffic data and website traffic trends?

Web traffic data focuses on point-in-time volume. Website traffic trends focus on the growth trajectory over time - whether a site is gaining or losing audience momentum.

### Can I use this for investor research?

Yes. Website traffic trends are a leading indicator of business performance for digital-first companies. Consistent traffic growth ahead of earnings often correlates with revenue growth.

---

## Related

- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [google-trends](https://trendsmcp.ai/google-trends)
- [amazon-product-data](https://trendsmcp.ai/amazon-product-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/website-traffic-trends](https://trendsmcp.ai/website-traffic-trends)*