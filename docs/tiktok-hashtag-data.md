---
title: "TikTok Hashtag Data API for AI via MCP | Trends MCP"
description: "Structured TikTok hashtag volume data for AI agents via MCP. Growth metrics, historical series, viral signal detection. No TikTok API key required."
canonical: "https://trendsmcp.ai/tiktok-hashtag-data"
---

# TikTok hashtag volume data for AI agents

> Structured TikTok hashtag data your AI can analyze, rank, and act on. Track which hashtags are growing, which are peaking, and which are fading - with normalized volume and growth rates per period.

**Full page with live demo:** [https://trendsmcp.ai/tiktok-hashtag-data](https://trendsmcp.ai/tiktok-hashtag-data)

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
get_growth(keyword='cleanbeauty', source='tiktok', percent_growth=['1M', '3M'])
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

### What does TikTok hashtag data look like in the response?

JSON with normalized interest (0-100), absolute volume estimate, growth percentage over the selected period, and a weekly time series array with dates and values.

### Can AI agents use TikTok data for product trend research?

Yes. A common workflow: give your AI a list of product categories as hashtags, have it call get_growth for each, and return a ranked table of which are growing fastest on TikTok.

### How does TikTok hashtag data compare to influencer metrics?

Hashtag volume data reflects total platform-level demand, not individual creator performance. It is a macro signal - useful for identifying category momentum rather than evaluating specific accounts.

---

## Related

- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [youtube-search-data](https://trendsmcp.ai/youtube-search-data)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/tiktok-hashtag-data](https://trendsmcp.ai/tiktok-hashtag-data)*