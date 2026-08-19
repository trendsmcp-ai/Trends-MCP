---
title: "News Sentiment Data for AI via MCP | Trends MCP"
description: "Query news sentiment and volume data from any AI assistant via MCP. Positive/negative sentiment scores, media volume trends, and topic coverage history."
canonical: "https://trendsmcp.ai/news-sentiment-data"
---

# News sentiment and volume data for AI

> Understand how the news is covering any topic - and whether that coverage is positive or negative. Sentiment scores, media volume trends, and historical coverage data structured for AI analysis.

**Full page with live demo:** [https://trendsmcp.ai/news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)

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
get_growth(keyword='tesla', source='news sentiment, news volume', percent_growth=['3M'])
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

### What news data does Trends MCP provide?

Two signals: news volume (how much coverage a topic is receiving) and news sentiment (whether that coverage skews positive, neutral, or negative). Both are normalized and returned as time series.

### How is sentiment scored?

Sentiment is derived from NLP analysis of news article headlines and summaries, scored on a scale from -1 (strongly negative) to +1 (strongly positive). Trends MCP normalizes this to a 0-100 scale for consistency.

### Can I track sentiment for a company over earnings periods?

Yes. Query a company name or ticker and the sentiment series will show how media tone shifted around earnings announcements, product launches, or regulatory events.

### Which news sources are included?

Major English-language news outlets, financial media, and technology publications. The signal aggregates across sources rather than tracking individual outlets.

---

## Related

- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)
- [news-volume-data](https://trendsmcp.ai/news-volume-data)
- [google-trends](https://trendsmcp.ai/google-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)*