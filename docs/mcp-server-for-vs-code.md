---
title: "Trends MCP Server for VS Code - Live Trend Data in VS Code | Trends MCP"
description: "Add live trend data to VS Code and GitHub Copilot via MCP. Query Google, TikTok, Reddit, YouTube, npm trends directly inside VS Code. No API keys needed."
canonical: "https://trendsmcp.ai/mcp-server-for-vs-code"
---

# Trends MCP for VS Code and GitHub Copilot

> VS Code supports MCP servers natively. Add Trends MCP and GitHub Copilot can query live trend data across Google, TikTok, YouTube, Reddit, npm, and more - directly inside your editor without switching context.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)

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
get_growth(keyword='typescript', source='npm, google search', percent_growth=['1Y'])
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

### How do I add Trends MCP to VS Code?

Two options: (1) Open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P) and run 'MCP: Add Server', then enter the Trends MCP URL. (2) Add the JSON snippet to .vscode/mcp.json in your project or to your user settings. VS Code uses a slightly different key format: use 'type': 'http' instead of 'transport': 'http'.

### Does it work with GitHub Copilot?

Yes. Once Trends MCP is added to VS Code, GitHub Copilot Chat can call all Trends MCP tools. Ask Copilot to check npm download trends, track keyword growth, or compare competitor web traffic directly in the chat.

### What is the VS Code config format?

VS Code uses a different JSON structure than other clients. Use: { "trends-mcp": { "type": "http", "url": "https://api.trendsmcp.ai/v1/mcp" } } inside the servers key of your mcp.json file.

### Can I use Trends MCP in VS Code extensions?

Trends MCP is available to any VS Code extension or feature that has access to MCP tool calls, including GitHub Copilot Chat, Copilot Edits, and any extension that uses the VS Code MCP API.

---

## Related

- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [npm-trends](https://trendsmcp.ai/npm-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)*