---
title: "Trends MCP Server for Windsurf - Live Trend Data in Windsurf AI | Trends MCP"
description: "Add live trend data to Windsurf via MCP. Query Google, TikTok, Reddit, YouTube trends inside Windsurf. Paste one config snippet and get started instantly."
canonical: "https://trendsmcp.ai/mcp-server-for-windsurf"
---

# Trends MCP for Windsurf

> Give Windsurf live trend data across Google, TikTok, YouTube, Reddit, Amazon, and 8 more sources. Paste one snippet into your Windsurf MCP config and start querying real-time trend data in your AI sessions immediately.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-windsurf](https://trendsmcp.ai/mcp-server-for-windsurf)

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
get_top_trends(source='tiktok', limit=10)
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

### How do I add Trends MCP to Windsurf?

Paste the JSON snippet into your Windsurf MCP config file. On Mac/Linux: ~/.codeium/windsurf/mcp_config.json. On Windows: %USERPROFILE%\.codeium\windsurf\mcp_config.json. Or use the Command Palette: Windsurf: Configure MCP Servers.

### Does Trends MCP work with Windsurf Cascade?

Yes. All Trends MCP tools are available inside Windsurf Cascade. You can ask Cascade to run trend queries as part of any research or analysis workflow.

### What trend data can Windsurf access?

All 12+ sources: Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia, News, Web Traffic, App Downloads, Steam, and npm. Full cross-platform trend comparison in a single query.

---

## Related

- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-windsurf](https://trendsmcp.ai/mcp-server-for-windsurf)*