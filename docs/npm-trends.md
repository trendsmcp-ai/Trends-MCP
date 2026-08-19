---
title: "npm Download Trends MCP - Package Data for AI Assistants | Trends MCP"
description: "Query live npm package download data from any AI via MCP. Track JavaScript library adoption, framework growth, and developer ecosystem trends."
canonical: "https://trendsmcp.ai/npm-trends"
---

# npm package trend data for AI assistants

> Track weekly download counts for any npm package. Package download trends reveal which JavaScript libraries and frameworks developers are adopting, which are losing ground, and where the ecosystem is heading.

**Full page with live demo:** [https://trendsmcp.ai/npm-trends](https://trendsmcp.ai/npm-trends)

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
get_trends(keyword='react', source='npm', data_mode='weekly')
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

### What npm data does Trends MCP return?

Weekly download counts for any npm package, normalized to a 0-100 scale, plus raw download volume, growth rates over standard periods (7D, 1M, 3M, 1Y), and a historical time series going back up to 5 years.

### How do I query a specific package?

Use the exact npm package name -- for example 'react', 'lodash', 'express', or '@anthropic-ai/sdk'. Scoped packages use the @org/package format.

### Can I compare multiple packages?

Yes. Use get_growth with comma-separated package names or call get_trends for each package and compare the normalized series. Useful for framework comparisons like React vs Vue vs Svelte.

### Why is npm data useful for investment research?

npm download trends are a leading indicator of developer ecosystem adoption. A library growing fast in downloads often precedes broader commercial adoption of the underlying platform or framework.

### How is npm download data normalized?

Raw weekly download counts are normalized to a 0-100 scale relative to the package's own historical peak. This makes it possible to compare adoption velocity across packages with very different absolute download volumes.

---

## Related

- [steam-trends](https://trendsmcp.ai/steam-trends)
- [app-download-trends](https://trendsmcp.ai/app-download-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/npm-trends](https://trendsmcp.ai/npm-trends)*