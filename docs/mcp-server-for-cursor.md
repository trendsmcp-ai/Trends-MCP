---
title: "Trends MCP Server for Cursor - Live Trend Data in Cursor AI | Trends MCP"
description: "Add live trend data to Cursor in seconds. Connect Trends MCP to Cursor and query Google, TikTok, Reddit, YouTube trends directly inside your IDE. One-click install."
canonical: "https://trendsmcp.ai/mcp-server-for-cursor"
---

# Trends MCP for Cursor

> Give Cursor live trend data across Google, TikTok, YouTube, Reddit, and 9 more sources. Click the install button below or paste a one-line config snippet into your MCP settings and start querying trend data inside Cursor immediately.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)

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
get_growth(keyword='vibe coding', source='google search, youtube, reddit', percent_growth=['3M'])
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

### How do I add Trends MCP to Cursor?

Click the '+ Add to Cursor' button on this page for one-click install. Or manually: paste the JSON snippet into ~/.cursor/mcp.json (Mac/Linux) or %USERPROFILE%\.cursor\mcp.json (Windows) under the mcpServers key. Restart Cursor.

### Does Trends MCP work with Cursor Agent mode?

Yes. All Trends MCP tools are available in Cursor Agent and Cursor Chat. You can ask Cursor to run get_trends, get_growth, or get_top_trends as part of any research or analysis task.

### What is Trends MCP useful for inside an IDE?

Common uses in Cursor: researching which npm packages or frameworks are gaining adoption (npm source), tracking whether a technology or product category is growing before building on it, and pulling competitor website traffic data directly into your analysis without leaving the editor.

### Can I use it in Cursor with a project-level config?

Yes. Place a .cursor/mcp.json file in your project root for project-scoped MCP servers, or edit ~/.cursor/mcp.json for global access across all projects.

---

## Related

- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)
- [npm-trends](https://trendsmcp.ai/npm-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)*