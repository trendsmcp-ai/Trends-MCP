---
title: "YouTube Search Volume Data for AI via MCP | Trends MCP"
description: "Access structured YouTube search volume data in your AI via MCP. Keyword demand over time, growth metrics, and normalized signals. No quota limits."
canonical: "https://trendsmcp.ai/youtube-search-data"
---

# YouTube search volume data for AI agents

> Structured YouTube keyword search volume delivered to your AI. Identify which topics are gaining traction on the world's largest video platform - with growth rates, time series, and cross-platform comparison built in.

**Full page with live demo:** [https://trendsmcp.ai/youtube-search-data](https://trendsmcp.ai/youtube-search-data)

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
get_growth(keyword='sourdough bread', source='youtube', percent_growth=['6M'])
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

### What format does YouTube search data come back in?

JSON with a normalized time series (0-100 scale), period-over-period growth percentage, absolute volume estimate, and a data quality score.

### Can I compare YouTube demand against TikTok for the same keyword?

Yes. Query both sources in a single get_growth call and the response includes side-by-side growth metrics - useful for understanding where audience attention is shifting.

### Is this useful for content marketers?

Yes. Content teams use it to validate whether a topic has growing YouTube search demand before investing in video production.

---

## Related

- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [google-search-data](https://trendsmcp.ai/google-search-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/youtube-search-data](https://trendsmcp.ai/youtube-search-data)*