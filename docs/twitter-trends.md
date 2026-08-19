---
title: "Twitter Trends MCP - Real-Time Social Signals for AI | Trends MCP"
description: "Query Twitter/X trend signals from any AI assistant via MCP. Track real-time social conversation volume, viral topics, and historical activity. Instant setup."
canonical: "https://trendsmcp.ai/twitter-trends"
---

# Twitter / X trend signals for AI assistants

> Track what is breaking on X / Twitter in real time. Social conversation volume, viral topic signals, and historical activity data - without the X API cost.

**Full page with live demo:** [https://trendsmcp.ai/twitter-trends](https://trendsmcp.ai/twitter-trends)

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
get_growth(keyword='bitcoin', source='google search, news volume, reddit', percent_growth=['3M'])
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

### How does Trends MCP get Twitter/X data?

X (Twitter) signals are derived from a combination of Google Search volume, news volume, and Reddit signals for the same topic, as X has restricted direct API access. Real-time X trending topics are also available via get_top_trends (source: 'X (Twitter)'), which surfaces what is breaking on X right now without a keyword.

### Is Twitter trend data real-time?

The signal updates daily. For real-time breakout detection, combine it with get_top_trends which surfaces what is spiking right now across all sources including X.

### Can I use this to track a brand's social presence?

Yes. Query a brand name or hashtag and the time series shows whether X conversation around that brand is growing or declining over your chosen period.

---

## Related

- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [x-trends](https://trendsmcp.ai/x-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/twitter-trends](https://trendsmcp.ai/twitter-trends)*