---
title: "X Trends MCP - Social Conversation Data for AI | Trends MCP"
description: "Access X (formerly Twitter) social trend data from your AI via MCP. Conversation volume, viral signals, topic momentum, and historical series."
canonical: "https://trendsmcp.ai/x-trends"
---

# X (formerly Twitter) trend data for AI agents

> Social conversation volume for any topic on X. Whether you are tracking a brand, a news story, or an emerging technology, X trend signals give your AI a pulse on real-time public discourse.

**Full page with live demo:** [https://trendsmcp.ai/x-trends](https://trendsmcp.ai/x-trends)

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
get_growth(keyword='openai', source='google search, news sentiment, reddit', percent_growth=['1M', '3M'])
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

### Why is the source called X but also Twitter?

The platform was rebranded from Twitter to X in 2023. Trends MCP supports both 'x' and 'twitter' as source values and returns the same signal for both.

### What does X/Twitter trend data measure?

Social conversation volume around a topic - how much discussion and engagement is happening on X relative to historical norms, normalized to a 0-100 scale.

### How does X trend data compare to Reddit?

X reflects fast-moving, real-time public conversation. Reddit tends to reflect deeper, community-based discussion. Comparing both reveals whether a topic is getting shallow viral attention or sustained community interest.

---

## Related

- [twitter-trends](https://trendsmcp.ai/twitter-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-discussion-data](https://trendsmcp.ai/reddit-discussion-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/x-trends](https://trendsmcp.ai/x-trends)*