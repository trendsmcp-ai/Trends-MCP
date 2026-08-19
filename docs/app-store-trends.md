---
title: "App Store Trends via MCP - Mobile Data for AI Agents | Trends MCP"
description: "Track app store trend signals from your AI via MCP. Mobile install growth, app ranking momentum, and category trends. Powered by Google Play data."
canonical: "https://trendsmcp.ai/app-store-trends"
---

# App store trend signals for AI agents

> Understand mobile app store momentum for any app or category. Which apps are climbing in installs? Which categories are growing fastest? App store trend data gives your AI mobile market intelligence without an app store API.

**Full page with live demo:** [https://trendsmcp.ai/app-store-trends](https://trendsmcp.ai/app-store-trends)

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
get_growth(keyword='com.openai.chatgpt', source='app downloads', percent_growth=['6M', '1Y'])
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

### How is app store trend data structured?

JSON with normalized install trend (0-100), growth percentage over the selected period, and a weekly time series. Includes a data quality score based on app install volume.

### Can I compare multiple apps side by side?

Yes. Call get_growth for each bundle ID and compare the results -- useful for competitive analysis of apps in the same category.

### Why do I need a bundle ID instead of the app name?

The underlying AppBrain data is indexed by Android package name (bundle ID), not display names. Example: 'com.whatsapp' for WhatsApp, 'com.instagram.android' for Instagram.

---

## Related

- [app-download-trends](https://trendsmcp.ai/app-download-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/app-store-trends](https://trendsmcp.ai/app-store-trends)*