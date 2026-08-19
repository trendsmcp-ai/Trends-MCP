---
title: "Trends MCP for Cline - Live Trend Data in Cline AI Agent | Trends MCP"
description: "Add live trend data to Cline via MCP. Query Google, TikTok, Reddit, YouTube trends inside Cline's autonomous agent. One config snippet, instant setup."
canonical: "https://trendsmcp.ai/mcp-server-for-cline"
---

# Trends MCP for Cline

> Give Cline live trend data across Google, TikTok, YouTube, Reddit, Amazon, npm, and 8 more sources. Cline's autonomous agent mode can call Trends MCP tools as part of multi-step research tasks -- querying, comparing, and reporting on trends without manual intervention.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-cline](https://trendsmcp.ai/mcp-server-for-cline)

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
get_top_trends(source='reddit', limit=10)
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

### Does Cline support MCP?

Yes. Cline is one of the most popular VS Code extensions for autonomous AI agents and has first-class MCP support. Add the Trends MCP config to Cline's MCP settings and all trend tools are immediately available in agent mode.

### How do I configure Trends MCP in Cline?

Open Cline settings in VS Code, navigate to the MCP section, and add a new server with the URL https://api.trendsmcp.ai/v1/mcp. Cline will discover all available tools automatically.

### Why is Trends MCP useful for autonomous agents?

Cline agents can use Trends MCP to autonomously research market trends, validate product ideas, track keyword momentum, or monitor brand mentions across platforms -- all as part of longer automated workflows without requiring human input at each step.

### Which Trends MCP tools work best in Cline agent mode?

get_growth (for automated trend comparison), get_top_trends (for discovering what is trending now), and get_trends (for time-series data). Cline can chain these into multi-step reports automatically.

---

## Related

- [mcp-server-for-cursor](https://trendsmcp.ai/mcp-server-for-cursor)
- [mcp-server-for-vs-code](https://trendsmcp.ai/mcp-server-for-vs-code)
- [developer-ecosystem-trends](https://trendsmcp.ai/developer-ecosystem-trends)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-cline](https://trendsmcp.ai/mcp-server-for-cline)*