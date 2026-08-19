---
title: "Viral Trend Detection for AI via MCP - Spot Trends Early | Trends MCP"
description: "Detect viral trends early with live data via MCP. TikTok spikes, Reddit momentum, Wikipedia page view surges -- all queryable by your AI before trends reach mainstream Google Search."
canonical: "https://trendsmcp.ai/viral-trend-detection"
---

# Viral trend detection for AI agents

> The best time to act on a trend is before it peaks. Trends MCP gives your AI early-warning signals from TikTok, Reddit, and Wikipedia -- platforms where trends emerge before they hit Google Search -- so you can spot and act on what is going viral 2-4 weeks ahead of mainstream.

**Full page with live demo:** [https://trendsmcp.ai/viral-trend-detection](https://trendsmcp.ai/viral-trend-detection)

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
get_top_trends(source='tiktok', limit=20)
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

### Which platforms give the earliest trend signals?

TikTok (viral spikes appear 2-4 weeks before Google Search), Reddit (enthusiast and early-adopter discussion precedes mainstream awareness), Wikipedia (information-seeking spikes 24-72 hours before Google Search surges), and News Volume (media attention often precedes broader public discovery). Trends MCP covers all four in one query.

### How do I find what is trending right now without knowing the keyword?

Use get_top_trends(source='tiktok') or get_top_trends(source='google search') to surface what is rising right now across a platform. No keyword needed -- the API returns the current top trending topics and their growth rates.

### Can I compare a trend's trajectory across multiple platforms?

Yes. Query a keyword across TikTok, Reddit, YouTube, and Google Search and compare the growth curves. A trend growing fast on TikTok but still low on Google Search is early-stage. A trend peaking on Google Search but declining on TikTok is late-stage.

### How far in advance can Trends MCP detect a trend?

TikTok typically leads Google Search by 2-4 weeks. Reddit and Wikipedia can lead by 1-3 days for news-driven topics. The combination gives you a multi-layer early warning system across different trend cycle speeds.

---

## Related

- [content-strategy](https://trendsmcp.ai/content-strategy)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)
- [news-volume-data](https://trendsmcp.ai/news-volume-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/viral-trend-detection](https://trendsmcp.ai/viral-trend-detection)*