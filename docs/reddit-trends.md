---
title: "Reddit Trends MCP - Community Discussion Data for AI | Trends MCP"
description: "Query Reddit discussion volume trends from any AI assistant via MCP. Track community interest, subreddit activity, and growing topics. No Reddit API limits."
canonical: "https://trendsmcp.ai/reddit-trends"
---

# Reddit discussion trend data for AI

> Measure how much Reddit is talking about any topic. Community discussion volume, growing subreddit interest, and historical activity data - all queryable from your AI without hitting Reddit API limits.

**Full page with live demo:** [https://trendsmcp.ai/reddit-trends](https://trendsmcp.ai/reddit-trends)

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
get_trends(keyword='electric vehicles', source='reddit', data_mode='weekly')
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

### What Reddit data does Trends MCP provide?

Reddit discussion volume trends - normalized interest in a topic across the platform over time, including growth rate and historical time series. Not raw post counts, but a normalized demand signal calibrated for trend comparison.

### Is this useful for tracking community sentiment around a brand?

For volume signals, yes. Trends MCP shows whether discussion around a brand is growing or shrinking. For sentiment, the News source gives sentiment scores; Reddit gives pure volume context.

### Can I track a specific subreddit?

The current signal is platform-wide Reddit discussion volume for a keyword. Subreddit-level filtering is on the roadmap.

### How does Reddit trend data complement Google Trends?

Reddit often reflects niche, enthusiast, and early-adopter communities before topics reach mainstream Google Search. Comparing both reveals whether interest is still underground or going mainstream.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-discussion-data](https://trendsmcp.ai/reddit-discussion-data)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/reddit-trends](https://trendsmcp.ai/reddit-trends)*