---
title: "Social Media Trends API for AI - TikTok, Reddit, YouTube via MCP | Trends MCP"
description: "Social media trends API for AI assistants. Get live TikTok hashtag trends, Reddit discussion volume, YouTube search trends, and Twitter mention data via MCP. One endpoint, all platforms."
canonical: "https://trendsmcp.ai/social-media-trends-api"
---

# Social media trends API for AI assistants

> Managing separate API integrations for TikTok, Reddit, YouTube, and Twitter is painful. Trends MCP consolidates all social media trend signals into a single MCP endpoint: normalized, comparable, and ready for your AI to query in natural language. One connection replaces four integrations.

**Full page with live demo:** [https://trendsmcp.ai/social-media-trends-api](https://trendsmcp.ai/social-media-trends-api)

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
get_growth(keyword='trending topic', source='tiktok, reddit, youtube, twitter', percent_growth=['1M', '3M'])
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

### Which social media platforms does Trends MCP cover?

TikTok (hashtag trends and video volume), Reddit (community discussion trends), YouTube (video search volume), Twitter/X (mention trends), LinkedIn (professional discussion trends), and News (social media coverage volume). All normalized to a comparable 0-100 scale.

### Why use a social media trends API instead of individual platform APIs?

Individual platform APIs have different rate limits, authentication systems, data schemas, and availability. TikTok's API is especially restricted. Trends MCP abstracts all of this into a single endpoint with a consistent schema, so your AI gets the data it needs without you managing multiple integrations.

### Is TikTok trend data available via API?

TikTok does not offer a public trends API. Trends MCP provides TikTok hashtag and trend data through a managed data pipeline, making it available to AI assistants when TikTok's own API does not expose this data.

### Can I compare a trend across all social platforms at once?

Yes. Use get_growth with source='tiktok, reddit, youtube, twitter' or source='all' to see how a keyword or topic is trending across every social platform simultaneously. This cross-platform view is one of Trends MCP's most powerful capabilities.

---

## Related

- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [twitter-trends](https://trendsmcp.ai/twitter-trends)
- [real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/social-media-trends-api](https://trendsmcp.ai/social-media-trends-api)*