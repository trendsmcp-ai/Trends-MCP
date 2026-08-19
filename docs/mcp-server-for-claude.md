---
title: "Trends MCP Server for Claude - Live Trend Data in Claude AI | Trends MCP"
description: "Add live trend data to Claude in 30 seconds. Connect Trends MCP to Claude Desktop or Claude.ai and query Google, TikTok, Reddit, YouTube trends directly in your conversations."
canonical: "https://trendsmcp.ai/mcp-server-for-claude"
---

# Trends MCP for Claude

> Give Claude live trend data across Google, TikTok, YouTube, Reddit, Amazon, and 8 more sources. Works with Claude Desktop and Claude.ai. Paste one config snippet and your conversations get real-time trend data instantly.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)

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
get_growth(keyword='ai agents', source='all', percent_growth=['3M', '1Y'])
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

### Does Trends MCP work with Claude.ai in the browser?

Yes. Claude.ai Pro, Max, and Team plans support remote MCP connections. Go to Settings → Connectors → Add custom connector and paste the Trends MCP URL. No JSON config needed.

### Does it work with Claude Desktop?

Yes. Add the config snippet to your claude_desktop_config.json file under mcpServers. On Mac: ~/Library/Application Support/Claude/claude_desktop_config.json. On Windows: %APPDATA%\Claude\claude_desktop_config.json. Fully quit and restart Claude Desktop after saving.

### Does it work with Claude Code?

Yes. Claude Code supports MCP servers. Add the same JSON snippet to your MCP configuration and all Trends MCP tools are available in your Claude Code sessions.

### What trend data can Claude access after connecting?

All 12+ sources: Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, News Sentiment, News Volume, Web Traffic, App Downloads, Steam, and npm. Use get_trends, get_growth, or get_top_trends to query any of them.

### Do I need separate API keys for each platform?

No. Trends MCP handles all source connectivity. You connect once and Claude can query all platforms immediately.

---

## Related

- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)
- [google-trends](https://trendsmcp.ai/google-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)*