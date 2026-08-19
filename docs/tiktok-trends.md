---
title: "TikTok Trends MCP - Live Hashtag Data for AI | Trends MCP"
description: "Query live TikTok hashtag trend data from any AI assistant via MCP. Track viral hashtags, growth spikes, and 5-year history. No TikTok API key needed."
canonical: "https://trendsmcp.ai/tiktok-trends"
---

# TikTok trend data for AI assistants

> Spot TikTok trends before they go mainstream. Track hashtag volume growth, viral spikes, and platform-specific demand signals - all accessible from your AI in plain language.

**Full page with live demo:** [https://trendsmcp.ai/tiktok-trends](https://trendsmcp.ai/tiktok-trends)

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
get_trends(keyword='booktok', source='tiktok', data_mode='weekly')
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

### What TikTok data does Trends MCP provide?

TikTok hashtag trend volume - normalized interest, growth rate, and historical time series. This reflects how frequently a hashtag appears and grows on the platform over time.

### How early can I detect a TikTok trend?

Trends MCP returns weekly and daily data. Daily data (last 30 days) lets you spot early-stage growth spikes before a hashtag reaches mainstream saturation.

### Can I compare TikTok trends against Google Search?

Yes. Query both sources in one call. TikTok often shows spikes 2-4 weeks before the same topic rises on Google Search, making cross-platform comparison a leading indicator strategy.

### Does this work for brand monitoring on TikTok?

Yes. Track a brand name or product hashtag over time to measure TikTok presence growth relative to competitors.

### Are TikTok hashtags case-sensitive?

No. The query is normalized before lookup. You can use 'booktok', 'BookTok', or '#booktok' - all return the same signal.

---

## Related

- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [tiktok-hashtag-data](https://trendsmcp.ai/tiktok-hashtag-data)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/tiktok-trends](https://trendsmcp.ai/tiktok-trends)*