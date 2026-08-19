---
title: "Wikipedia Trends MCP - Page View Data for AI | Trends MCP"
description: "Query Wikipedia page view trends from any AI assistant via MCP. Track information-seeking spikes, rising topics, and historical page traffic. Instant setup."
canonical: "https://trendsmcp.ai/wikipedia-trends"
---

# Wikipedia page view trend data for AI

> Wikipedia page views reveal what the world is suddenly curious about. Spike detection, historical page traffic, and cross-platform comparison - giving your AI a unique information-demand signal that precedes mainstream search.

**Full page with live demo:** [https://trendsmcp.ai/wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)

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
get_trends(keyword='quantum computing', source='wikipedia', data_mode='weekly')
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

### What Wikipedia data does Trends MCP provide?

Wikipedia page view trends - normalized traffic to the Wikipedia article for a given topic over time. This is a strong information-demand signal: when something breaks in the news, Wikipedia views spike before Google Search catches up.

### How is Wikipedia data useful as a trend signal?

Wikipedia spikes often lead Google Trends by 24-72 hours for news-driven events. It is a leading indicator of public curiosity - useful for media, research, and investment applications.

### Does it track the English Wikipedia only?

Yes, currently English Wikipedia page views are tracked. Multi-language support is on the roadmap.

### Can I track a person, company, or event?

Yes. Any topic with a Wikipedia article can be tracked. Company pages, political figures, scientific concepts, and current events all work.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [wikipedia-page-views](https://trendsmcp.ai/wikipedia-page-views)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)*