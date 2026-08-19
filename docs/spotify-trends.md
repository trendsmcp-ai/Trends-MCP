---
title: "Spotify Trends via MCP - Music and Podcast Search Data for AI | Trends MCP"
description: "Query Spotify-related trend data from any AI assistant via MCP. Track music genre momentum, podcast topic interest, and audio content demand via Google Search signals."
canonical: "https://trendsmcp.ai/spotify-trends"
---

# Spotify and audio trend data for AI assistants

> Track music genre momentum, podcast topic interest, and artist search trends. Spotify-related demand signals derived from Google Search volume reveal what audio content audiences are seeking before listening platforms surface it in their own charts.

**Full page with live demo:** [https://trendsmcp.ai/spotify-trends](https://trendsmcp.ai/spotify-trends)

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
get_growth(keyword='afrobeats site:spotify.com', source='google search', percent_growth=['1Y', '3M'])
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

### How does Trends MCP access Spotify data?

Spotify trends are derived from Google Search volume for Spotify-related queries, as Spotify does not offer a public trends API. This reflects demand for specific artists, genres, or podcast topics within the Spotify context.

### What is Spotify trend data useful for?

Music industry research (rising genres, emerging artists), podcast content strategy (growing topic categories), audio advertising planning, and entertainment investment research where music or audio trends signal broader cultural momentum.

### Can I track a specific artist or podcast?

Yes. Query an artist name or podcast title and the signal shows whether search interest within Spotify contexts is growing or declining -- useful for tracking emerging artists before they chart.

---

## Related

- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [google-search-trends](https://trendsmcp.ai/google-search-trends)
- [content-strategy](https://trendsmcp.ai/content-strategy)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/spotify-trends](https://trendsmcp.ai/spotify-trends)*