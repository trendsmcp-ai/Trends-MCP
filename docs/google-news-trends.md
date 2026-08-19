---
title: "Google News Trends via MCP - News Search Volume for AI | Trends MCP"
description: "Query Google News search trends from any AI assistant via MCP. Track news topic volume, breaking story detection, and media coverage momentum. No API key needed."
canonical: "https://trendsmcp.ai/google-news-trends"
---

# Google News trend data for AI assistants

> Track what people are searching for in Google News. Breaking story volume, emerging coverage topics, and news interest momentum -- structured data your AI can use to detect when a story is gaining media traction before it reaches peak saturation.

**Full page with live demo:** [https://trendsmcp.ai/google-news-trends](https://trendsmcp.ai/google-news-trends)

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
get_trends(keyword='federal reserve', source='google news', data_mode='weekly')
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

### What is Google News trend data?

Google News search volume reflects how many people are actively searching for a topic within Google News specifically -- a signal of breaking news interest rather than general information-seeking. It spikes sharply when a story breaks and declines as coverage fades.

### How is Google News data different from News Sentiment data?

Google News trend data measures search demand for a topic in the news context. News Sentiment data measures the tone (positive/negative) and volume of actual news articles published about a topic. Together they reveal both how much public attention a story is getting and whether coverage is favorable.

### Can I detect a breaking news story early with this data?

Yes. A sudden spike in Google News search volume often precedes the peak of broader Google Search interest by a few hours to a day. Combine with Wikipedia page view spikes for an early-warning signal stack.

---

## Related

- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [news-volume-data](https://trendsmcp.ai/news-volume-data)
- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-news-trends](https://trendsmcp.ai/google-news-trends)*