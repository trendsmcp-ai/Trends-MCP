---
title: "App Download Trends MCP - Mobile Growth Data for AI | Trends MCP"
description: "Query app download trend data from any AI assistant via MCP. Track mobile app growth, install spikes, and historical download signals via Google Play."
canonical: "https://trendsmcp.ai/app-download-trends"
---

# App download trend data for AI assistants

> Track mobile app growth signals for any app or category. Download trend data reveals which apps are gaining users, which categories are booming, and where mobile consumer attention is shifting.

**Full page with live demo:** [https://trendsmcp.ai/app-download-trends](https://trendsmcp.ai/app-download-trends)

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
get_trends(keyword='com.duolingo', source='app downloads', data_mode='weekly')
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

### What app download data does Trends MCP provide?

Normalized Android app install trend data sourced from Google Play via AppBrain estimates. Returns download growth trends, historical time series, and growth rates for individual apps.

### What format does the keyword need to be in?

You must use the Android bundle ID (package name), not the display name. For example: 'com.duolingo' for Duolingo, 'com.openai.chatgpt' for ChatGPT. Find it in the Google Play URL: play.google.com/store/apps/details?id=THIS_PART.

### Does this cover iOS App Store as well?

Currently the signal is sourced from Google Play (Android) via AppBrain. iOS App Store data is on the roadmap.

### Is this useful for mobile market research?

Yes. Investors, product teams, and market researchers use app download trends to measure user adoption velocity and identify emerging mobile-first businesses.

---

## Related

- [app-store-trends](https://trendsmcp.ai/app-store-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/app-download-trends](https://trendsmcp.ai/app-download-trends)*