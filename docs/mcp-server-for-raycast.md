---
title: "Trends MCP for Raycast - Live Trend Data in Raycast AI | Trends MCP"
description: "Add live trend data to Raycast AI via MCP. Query Google, TikTok, Reddit, YouTube trends directly in Raycast. Instant setup for Mac power users."
canonical: "https://trendsmcp.ai/mcp-server-for-raycast"
---

# Trends MCP for Raycast

> Raycast AI supports MCP servers natively. Add Trends MCP and you can query live trend data across Google, TikTok, YouTube, Reddit, Amazon, and more directly from the Raycast command bar -- the fastest way to research trends on a Mac.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-raycast](https://trendsmcp.ai/mcp-server-for-raycast)

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
get_top_trends(source='google search', limit=10)
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

### Does Raycast support MCP?

Yes. Raycast AI has native MCP support. You can add any remote MCP server including Trends MCP directly from Raycast's AI settings or Extensions preferences.

### How do I add Trends MCP to Raycast?

Open Raycast Settings → Extensions → AI → MCP Servers. Add a new server and enter the Trends MCP URL: https://api.trendsmcp.ai/v1/mcp. All trend tools are immediately available in Raycast AI.

### What makes Trends MCP useful in Raycast?

Raycast is built for quick lookups and fast workflows. With Trends MCP connected, you can check what is trending on Google, TikTok, or Reddit in seconds from anywhere on your Mac -- without opening a browser or switching apps.

### Can Raycast AI run multi-source trend comparisons?

Yes. Use get_growth with source='all' in Raycast AI to get cross-platform trend comparison across all 12+ sources in a single query.

---

## Related

- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-raycast](https://trendsmcp.ai/mcp-server-for-raycast)*