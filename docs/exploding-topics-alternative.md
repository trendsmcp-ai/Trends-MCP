---
title: "Exploding Topics Alternative - Live Trend Data via MCP | Trends MCP"
description: "An Exploding Topics alternative built for AI agents. Real-time trend data across 12+ platforms via MCP. Query any keyword on demand, not just curated lists."
canonical: "https://trendsmcp.ai/exploding-topics-alternative"
---

# An Exploding Topics alternative for AI agents

> Exploding Topics curates a fixed set of trending topics updated periodically. Trends MCP lets your AI query any keyword, on any platform, in real time -- Google, TikTok, YouTube, Reddit, Amazon, Wikipedia, and more. No waiting for a weekly digest.

**Full page with live demo:** [https://trendsmcp.ai/exploding-topics-alternative](https://trendsmcp.ai/exploding-topics-alternative)

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
get_growth(keyword='agentic ai', source='google search, tiktok, reddit, youtube', percent_growth=['1M', '3M', '1Y'])
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

### How is Trends MCP different from Exploding Topics?

Exploding Topics curates a database of hand-selected trending topics and surfaces them through a browsable interface. Trends MCP is a query tool: you ask about any keyword you choose and get live data back instantly across 12+ platforms. Trends MCP is for AI-agent workflows; Exploding Topics is for human browsing and discovery.

### Can I discover trending topics without knowing the keyword first?

Yes. Use get_top_trends(source='tiktok') or get_top_trends(source='google search') to surface what is rising right now across a platform without specifying a keyword -- similar to Exploding Topics' discovery mode but queryable by your AI in real time.

### Does Trends MCP have an API like Exploding Topics Pro?

Trends MCP delivers data via the Model Context Protocol, which is compatible with Claude, Cursor, VS Code, Windsurf, and other AI clients. If you need raw API access for programmatic integration, contact us.

### Is Trends MCP better for investors or market researchers?

For AI-agent workflows, yes. Trends MCP covers platforms that Exploding Topics does not: Amazon purchase intent, Wikipedia information spikes, news sentiment, web traffic trends, app download signals, and npm developer ecosystem data -- all queryable by your AI agent in a single session.

---

## Related

- [google-trends-alternative](https://trendsmcp.ai/google-trends-alternative)
- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [data-sources](https://trendsmcp.ai/data-sources)
- [market-research](https://trendsmcp.ai/market-research)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/exploding-topics-alternative](https://trendsmcp.ai/exploding-topics-alternative)*