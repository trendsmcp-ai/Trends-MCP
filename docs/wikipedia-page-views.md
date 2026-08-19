---
title: "Wikipedia Page Views Data for AI via MCP | Trends MCP"
description: "Structured Wikipedia page view data for AI agents via MCP. Information-seeking volume, spike detection, and historical traffic series. No setup required."
canonical: "https://trendsmcp.ai/wikipedia-page-views"
---

# Wikipedia page view data for AI agents

> Structured Wikipedia traffic data for any topic, delivered to your AI. Measure information-seeking volume, detect sudden spikes from news events, and correlate with search and social signals across the same timeline.

**Full page with live demo:** [https://trendsmcp.ai/wikipedia-page-views](https://trendsmcp.ai/wikipedia-page-views)

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
get_growth(keyword='nuclear fusion', source='wikipedia', percent_growth=['3M'])
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

### What does Wikipedia page view data look like?

JSON with normalized page traffic (0-100), absolute view count estimates, growth percentage, and a weekly time series. Includes a data quality score based on article traffic volume.

### Can I use this to detect breaking news topics?

Yes. A sudden spike in Wikipedia page views is often the earliest detectable signal that a topic has entered public consciousness. Combine with get_top_trends for real-time detection.

---

## Related

- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/wikipedia-page-views](https://trendsmcp.ai/wikipedia-page-views)*