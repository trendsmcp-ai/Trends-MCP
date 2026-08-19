---
title: "Facebook Trends MCP - Social Data for AI Assistants | Trends MCP"
description: "Track Facebook and broader social media trends via MCP. Monitor brand mentions, topic interest, and social demand signals for AI assistants. Cross-platform social trend data."
canonical: "https://trendsmcp.ai/facebook-trends"
---

# Facebook and social media trends for AI assistants

> Facebook does not offer a public trends API, but the signals are in the data. Trends MCP triangulates social trend momentum using News sentiment and volume, Reddit discussion trends, and cross-platform search signals -- giving your AI a proxy for Facebook-level social interest without requiring Facebook API access.

**Full page with live demo:** [https://trendsmcp.ai/facebook-trends](https://trendsmcp.ai/facebook-trends)

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
get_growth(keyword='brand name', source='news sentiment, reddit, google search', percent_growth=['3M'])
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

### Does Trends MCP have direct Facebook data?

Facebook does not provide a public trends API. Trends MCP covers social trend signals through Reddit (community discussion volume), News sentiment and volume, Twitter/X, and cross-platform search data. These sources together give a strong proxy for social media interest trends.

### What social platforms does Trends MCP cover?

Reddit, Twitter/X, LinkedIn, TikTok, YouTube, and News (across thousands of outlets). Together these cover the major social trend signals available through legitimate data access.

### How can I track a brand's social trend momentum?

Use get_growth with source='reddit, news sentiment, twitter' to see discussion and mention volume trends for a brand over time. This is particularly useful for brand monitoring, PR teams, and investment research.

### What about Instagram trends?

Instagram's API does not expose public trend data. TikTok hashtag data from Trends MCP is a strong proxy for visual content trends, as TikTok and Instagram Reels content trend cycles are closely correlated.

---

## Related

- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [twitter-trends](https://trendsmcp.ai/twitter-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [brand-monitoring](https://trendsmcp.ai/brand-monitoring)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/facebook-trends](https://trendsmcp.ai/facebook-trends)*