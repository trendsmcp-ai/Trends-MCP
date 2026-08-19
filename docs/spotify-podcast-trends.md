---
title: "Spotify & Podcast Trends MCP - Audio Trend Data for AI | Trends MCP"
description: "Track Spotify music trends and podcast topic momentum via MCP. Audio trend data for AI assistants: what is trending in music, podcasts, and audio content."
canonical: "https://trendsmcp.ai/spotify-podcast-trends"
---

# Spotify and podcast trends for AI assistants

> Music and podcasts are leading cultural indicators -- what is trending on Spotify often predicts what will trend everywhere else. Trends MCP gives your AI access to Spotify trend signals alongside YouTube audio content search volume and News coverage of artists, genres, and podcast topics.

**Full page with live demo:** [https://trendsmcp.ai/spotify-podcast-trends](https://trendsmcp.ai/spotify-podcast-trends)

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
get_growth(keyword='true crime podcast', source='youtube, google search, news sentiment', percent_growth=['3M'])
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

### What Spotify trend data is available via MCP?

Trends MCP covers Spotify trend signals including artist search interest, genre momentum, and podcast topic trends. These are complemented by YouTube audio search volume and broader Google Search trends for music and podcast topics.

### Who uses podcast and audio trend data?

Podcast producers identifying trending topics to cover, music industry analysts tracking emerging genres and artists, content marketers identifying audio formats gaining traction, and media researchers studying how audio trends relate to broader cultural shifts.

### Can I track a specific artist or podcast?

Yes. Use get_growth or get_trends with an artist name or podcast title to track its search and social momentum over time across platforms.

### How does podcast trend data complement other sources?

Podcast topics often appear in search 3-6 months after first gaining traction in podcast conversations. Tracking both podcast trend data and Google Search volume gives a leading-lagging indicator pair useful for content strategy.

---

## Related

- [spotify-trends](https://trendsmcp.ai/spotify-trends)
- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [content-strategy](https://trendsmcp.ai/content-strategy)
- [viral-trend-detection](https://trendsmcp.ai/viral-trend-detection)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/spotify-podcast-trends](https://trendsmcp.ai/spotify-podcast-trends)*