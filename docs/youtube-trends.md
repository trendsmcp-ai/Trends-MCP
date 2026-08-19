---
title: "YouTube Trends MCP - Live Video Search Data for AI | Trends MCP"
description: "Query YouTube search volume trends from any AI assistant via MCP. Track rising video topics, keyword demand, and 5-year history. No YouTube API quota limits."
canonical: "https://trendsmcp.ai/youtube-trends"
---

# YouTube trend data for AI assistants

> Find out what people are searching for on YouTube. Rising topics, growing video keywords, and historical search demand - all queryable by your AI in plain language.

**Full page with live demo:** [https://trendsmcp.ai/youtube-trends](https://trendsmcp.ai/youtube-trends)

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
get_trends(keyword='morning routine', source='youtube', data_mode='weekly')
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

### What YouTube data does Trends MCP provide?

YouTube video search volume trends - normalized interest over time, growth metrics, and historical series. This reflects demand for video content on specific topics, not view counts on individual videos.

### How is YouTube search data different from Google Search data?

YouTube reflects video-specific intent. A keyword like 'how to do a handstand' may have high YouTube demand but lower Google Search volume. Comparing both reveals content format preferences.

### Can I use this to find trending YouTube content ideas?

Yes. Query a set of topic keywords, rank by growth rate over the last 30 days, and your AI will surface which video topics are gaining search momentum right now.

### Does it cover YouTube Shorts search demand?

The signal reflects overall YouTube search volume including Shorts discovery. YouTube does not separate Shorts search data, so results reflect total platform search interest.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [youtube-search-data](https://trendsmcp.ai/youtube-search-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/youtube-trends](https://trendsmcp.ai/youtube-trends)*