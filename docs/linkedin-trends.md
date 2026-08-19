---
title: "LinkedIn Trends via MCP - Professional Topic Data for AI | Trends MCP"
description: "Query LinkedIn topic trends from any AI assistant via MCP. Track professional interest in business topics, skills, and industry keywords. Via Google Search signals."
canonical: "https://trendsmcp.ai/linkedin-trends"
---

# LinkedIn topic trend data for AI assistants

> Measure professional and B2B interest in any topic. LinkedIn trend signals reveal what business audiences are actively discussing and searching - useful for B2B content strategy, hiring signals, and industry momentum tracking.

**Full page with live demo:** [https://trendsmcp.ai/linkedin-trends](https://trendsmcp.ai/linkedin-trends)

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
get_growth(keyword='generative AI site:linkedin.com', source='google search', percent_growth=['1Y', '3M'])
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

### How does Trends MCP access LinkedIn data?

LinkedIn trends are derived from Google Search volume for LinkedIn-specific queries (using 'google search' as the source). LinkedIn does not offer a public trends API, so this signal reflects the volume of searches for professional topics associated with LinkedIn content and discussions.

### What is LinkedIn trend data useful for?

B2B content strategy, tracking which professional skills or technologies are gaining traction, monitoring competitor brand presence in professional contexts, and identifying emerging industry conversations.

### How does LinkedIn trend data differ from Google Trends?

LinkedIn signals reflect professional and B2B intent specifically. A keyword like 'supply chain automation' may have modest Google Search volume but strong LinkedIn trend signals, indicating strong B2B industry interest.

---

## Related

- [google-search-trends](https://trendsmcp.ai/google-search-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/linkedin-trends](https://trendsmcp.ai/linkedin-trends)*