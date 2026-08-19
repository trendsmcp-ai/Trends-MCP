---
title: "Google Search Trends via MCP - Keyword Volume for AI | Trends MCP"
description: "Give AI assistants access to Google Search trend data via MCP. Track keyword search volume over time, spot rising queries, and compare growth across any period."
canonical: "https://trendsmcp.ai/google-search-trends"
---

# Google Search trend data via MCP

> Track how Google Search volume for any keyword has moved over time. Period-over-period growth, rising queries, and declining signals - structured data your AI can act on directly.

**Full page with live demo:** [https://trendsmcp.ai/google-search-trends](https://trendsmcp.ai/google-search-trends)

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
get_growth(keyword='weight loss supplements', source='google search', percent_growth=['3M', '1Y'])
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

### How is Google Search trend data different from Google Trends?

Google Trends shows relative popularity. Google Search trend data in Trends MCP adds absolute query volume estimates, precise percentage growth calculations, and structured JSON output - making it actionable for AI agents doing research or monitoring.

### What growth periods are available?

7 days, 1 month, 3 months, 6 months, 1 year, year-to-date, and custom date ranges. The API returns start date, end date, volume for each period, and percentage change.

### Can I track multiple keywords at once?

Yes. Pass a list of keywords and get comparative growth metrics back in a single structured response, sorted by growth rate.

### Is this useful for SEO keyword research?

Yes. You can ask your AI to identify which keywords in a list are growing fastest on Google Search, then use that to prioritize content or ad spend.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [google-search-data](https://trendsmcp.ai/google-search-data)
- [youtube-trends](https://trendsmcp.ai/youtube-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/google-search-trends](https://trendsmcp.ai/google-search-trends)*