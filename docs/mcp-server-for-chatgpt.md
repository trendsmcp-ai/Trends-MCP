---
title: "Trends MCP for ChatGPT - Live Trend Data in ChatGPT | Trends MCP"
description: "Connect Trends MCP to ChatGPT for live trend data. Query Google, TikTok, Reddit, YouTube trends directly in ChatGPT. Setup guide for ChatGPT MCP integration."
canonical: "https://trendsmcp.ai/mcp-server-for-chatgpt"
---

# Trends MCP for ChatGPT

> OpenAI has adopted the Model Context Protocol standard. Connect Trends MCP to ChatGPT and your conversations gain access to live trend data across Google, TikTok, YouTube, Reddit, Amazon, and 8 more sources -- giving ChatGPT current data beyond its training cutoff.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-chatgpt](https://trendsmcp.ai/mcp-server-for-chatgpt)

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
get_growth(keyword='openai o3', source='google search, reddit', percent_growth=['3M'])
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

### Does ChatGPT support MCP?

Yes. OpenAI adopted the Model Context Protocol standard in 2025. ChatGPT can connect to remote MCP servers including Trends MCP. Check your ChatGPT settings for the MCP or connectors section to add the Trends MCP URL.

### What can ChatGPT do with Trends MCP connected?

ChatGPT can query live trend data beyond its training cutoff: what is trending on Google right now, which TikTok topics are growing, which products are gaining Amazon search volume, and more. This gives ChatGPT current-world awareness it otherwise lacks.

### Is setup different for ChatGPT vs Claude?

Yes. ChatGPT uses its own connector UI rather than a JSON config file. Add the Trends MCP URL (https://api.trendsmcp.ai/v1/mcp) in ChatGPT's integrations or connectors section. The underlying protocol is the same MCP standard.

### Does it work with ChatGPT Plus, Team, and Enterprise?

MCP support in ChatGPT is available to Plus and higher tiers. Enterprise users may need their admin to allowlist external MCP servers.

---

## Related

- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [google-trends](https://trendsmcp.ai/google-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-chatgpt](https://trendsmcp.ai/mcp-server-for-chatgpt)*