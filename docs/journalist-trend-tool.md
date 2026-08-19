---
title: "Trending Topics Tool for Journalists - Live Data via MCP | Trends MCP"
description: "Real-time trending topics tool for journalists and newsrooms. Track what is gaining momentum on Google, Reddit, TikTok, and News via AI and MCP. Stay ahead of the story."
canonical: "https://trendsmcp.ai/journalist-trend-tool"
---

# Trending topics tool for journalists

> The best stories follow the momentum. Trends MCP gives journalists and newsrooms a live window into what is gaining traction across Google Search, Reddit, TikTok, YouTube, and News -- before it becomes the obvious headline. Spot the story, validate the interest, and report with data.

**Full page with live demo:** [https://trendsmcp.ai/journalist-trend-tool](https://trendsmcp.ai/journalist-trend-tool)

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
get_top_trends(source='google search, reddit', limit=20)
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

### How do journalists use trend data for story discovery?

Monitor get_top_trends daily across Google, Reddit, and TikTok to surface topics gaining rapid interest. A Reddit thread gaining 300% discussion volume is often a story 48 hours before mainstream outlets cover it. Trends MCP gives you that early signal.

### Can I track whether a story is gaining or losing momentum?

Yes. Use get_growth for a topic with 1-week and 1-month comparisons to see whether interest is accelerating, stable, or fading. Useful for deciding whether to follow up on a story or move on.

### Can I track news sentiment for a topic?

Yes. The News Sentiment source returns positive/negative/neutral scores alongside volume. Track whether coverage of a topic is becoming more negative over time -- useful for spotting emerging controversies.

### Is this useful for data journalism?

Yes. Trends MCP provides quantified trend signals that can be cited in data journalism pieces: 'Search interest in X grew 340% over the past three months', backed by cross-platform data.

---

## Related

- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [news-volume-data](https://trendsmcp.ai/news-volume-data)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [social-listening-ai](https://trendsmcp.ai/social-listening-ai)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/journalist-trend-tool](https://trendsmcp.ai/journalist-trend-tool)*