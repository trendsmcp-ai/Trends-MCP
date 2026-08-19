---
title: "Trends MCP for GitHub Copilot - Live Trend Data in VS Code | Trends MCP"
description: "Add live trend data to GitHub Copilot via MCP. Query Google, TikTok, Reddit, YouTube, npm trends directly in GitHub Copilot Chat inside VS Code. No API keys."
canonical: "https://trendsmcp.ai/mcp-server-for-github-copilot"
---

# Trends MCP for GitHub Copilot

> GitHub Copilot supports MCP servers via VS Code. Add Trends MCP and Copilot Chat can query live trend data across Google, TikTok, YouTube, Reddit, npm, and more -- without leaving your editor.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-github-copilot](https://trendsmcp.ai/mcp-server-for-github-copilot)

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
get_growth(keyword='rust programming', source='npm, google search', percent_growth=['1Y'])
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

### Does GitHub Copilot support MCP?

Yes. GitHub Copilot Chat in VS Code supports MCP servers. Add Trends MCP to your VS Code mcp.json and Copilot can call all Trends MCP tools directly from the chat panel.

### How do I set it up?

Add the Trends MCP config to .vscode/mcp.json in your project or to your VS Code user settings. Use the key format: { "trends-mcp": { "type": "http", "url": "https://api.trendsmcp.ai/v1/mcp" } } inside the servers key.

### What can Copilot do with trend data?

Ask Copilot to check npm download momentum before choosing a dependency, track whether a programming language or framework is growing, or pull competitor web traffic data directly into your analysis -- all without switching tabs.

### Is Trends MCP different from GitHub's own MCP server?

Yes. GitHub's official MCP server gives Copilot access to GitHub repositories and issues. Trends MCP gives Copilot access to live trend data from Google, TikTok, Reddit, YouTube, Amazon, npm, and 8 more sources. They complement each other.

---

## Related

- [mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)
- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [npm-trends](https://trendsmcp.ai/npm-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-github-copilot](https://trendsmcp.ai/mcp-server-for-github-copilot)*