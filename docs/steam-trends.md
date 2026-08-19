---
title: "Steam Trends MCP - Game Player Data for AI Assistants | Trends MCP"
description: "Query live Steam concurrent player data from any AI via MCP. Track game momentum, player count trends, and launch spikes for any game on Steam."
canonical: "https://trendsmcp.ai/steam-trends"
---

# Steam player trend data for AI assistants

> Track concurrent player counts and game momentum for any title on Steam. Player trend data reveals which games are growing, which are declining, and when major launches or updates are driving spikes.

**Full page with live demo:** [https://trendsmcp.ai/steam-trends](https://trendsmcp.ai/steam-trends)

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
get_trends(keyword='Counter-Strike 2', source='steam', data_mode='weekly')
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

### What Steam data does Trends MCP return?

Normalized concurrent player count trends (0-100 scale) for any game on Steam. Returns weekly time series, growth rates, and peak player data. Useful for tracking game momentum before and after launches, updates, or sales events.

### How do I identify a game for the query?

Use the game's display name as it appears on Steam -- for example 'Counter-Strike 2', 'Palworld', or 'Elden Ring'. The MCP server resolves the name to the correct Steam App ID automatically.

### What is a concurrent player count?

The number of players actively in-game at the same time, tracked by Steam. Peak concurrent players (PCU) is a standard metric for measuring a game's popularity and live engagement level.

### How is this useful for investment or market research?

Game studios, investors, and analysts use Steam player trends to gauge a title's commercial momentum, identify breakout games early, and track how a game retains players over time.

### How far back does the data go?

Up to 5 years of weekly data, giving you full launch history, seasonal cycles, and long-term retention trends for any game on Steam.

---

## Related

- [npm-trends](https://trendsmcp.ai/npm-trends)
- [app-download-trends](https://trendsmcp.ai/app-download-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/steam-trends](https://trendsmcp.ai/steam-trends)*