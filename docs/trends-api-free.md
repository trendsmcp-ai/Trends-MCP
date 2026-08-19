---
title: "Trends API Free Tier - Try Live Trend Data via MCP | Trends MCP"
description: "Try the Trends MCP API free. Get live trend data from Google, TikTok, Reddit, YouTube, and more via MCP. Free tier available for AI assistants and developers."
canonical: "https://trendsmcp.ai/trends-api-free"
---

# Try the trends API free

> Getting started with Trends MCP is free. Connect your AI assistant and run live trend queries across Google, TikTok, Reddit, YouTube, Amazon, and more -- no credit card required to explore. Upgrade for higher volumes and more sources when you are ready.

**Full page with live demo:** [https://trendsmcp.ai/trends-api-free](https://trendsmcp.ai/trends-api-free)

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
get_growth(keyword='test keyword', source='google search', percent_growth=['3M'])
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

### Is there a free tier for Trends MCP?

Yes. You can connect Trends MCP to your AI assistant and run trend queries at no cost to explore the data. The free tier includes access to core sources and query tools. Volume limits apply for free tier users.

### What is included in the free tier?

Free tier users can query core trend data sources including Google Search trends, and use the main query tools: get_trends, get_growth, and get_top_trends. Additional sources and higher query volumes are available on paid plans.

### Do I need a credit card to get started?

No. You can connect Trends MCP to your AI assistant and run queries immediately without providing payment details. If you exceed free tier limits, you will be prompted to upgrade.

### How do I get started for free?

Add the Trends MCP config snippet to your AI client (Claude, Cursor, VS Code, etc.) and you are connected immediately. The setup takes less than 30 seconds and requires no account creation to try.

---

## Related

- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [google-trends-api](https://trendsmcp.ai/google-trends-api)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/trends-api-free](https://trendsmcp.ai/trends-api-free)*