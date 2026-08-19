---
title: "Glimpse Alternative - Trend Data for AI Agents via MCP | Trends MCP"
description: "An alternative to Glimpse for AI-powered trend research. Get absolute Google Search volume, multi-platform signals, and real-time data via MCP. No browser extension needed."
canonical: "https://trendsmcp.ai/glimpse-alternative"
---

# A Glimpse alternative for AI agents

> Glimpse supercharges Google Trends with absolute volume data and channel breakdowns -- inside your browser. Trends MCP does the same thing directly inside your AI assistant, across 12+ platforms, without a browser extension or manual lookups.

**Full page with live demo:** [https://trendsmcp.ai/glimpse-alternative](https://trendsmcp.ai/glimpse-alternative)

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
get_growth(keyword='gut health', source='google search, tiktok, youtube, reddit', percent_growth=['3M', '1Y'])
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

### How does Trends MCP compare to Glimpse?

Glimpse is a Chrome extension that overlays absolute search volume data on top of Google Trends in your browser. Trends MCP delivers the same absolute volume data -- plus TikTok, Reddit, YouTube, Amazon, Wikipedia, news, and web traffic signals -- directly to your AI assistant without any browser extension.

### Does Trends MCP provide absolute Google Search volume like Glimpse?

Yes. Trends MCP returns absolute query volume estimates alongside normalized interest scores. The methodology is similar to Glimpse: combining Google Trends relative data with third-party search volume calibration.

### Can my AI get the channel breakdown that Glimpse shows?

Yes. Trends MCP covers the same channels Glimpse tracks (Google Search, YouTube, TikTok, Reddit, Pinterest interest) plus additional sources Glimpse does not: Amazon purchase intent, Wikipedia page views, news sentiment, web traffic trends, app downloads, Steam player counts, and npm developer downloads.

### Is Trends MCP useful for the same use cases as Glimpse?

Yes -- SEO keyword research, content strategy, e-commerce product research, and market trend analysis all work via Trends MCP. The key difference is that Trends MCP is designed for AI agents: your AI runs the queries and reasons over the data, rather than you manually looking up keywords in a browser extension.

---

## Related

- [google-trends-alternative](https://trendsmcp.ai/google-trends-alternative)
- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [exploding-topics-alternative](https://trendsmcp.ai/exploding-topics-alternative)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/glimpse-alternative](https://trendsmcp.ai/glimpse-alternative)*