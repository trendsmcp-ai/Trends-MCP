---
title: "News Volume Data for AI via MCP | Trends MCP"
description: "Track how much news coverage any topic is getting via MCP. Media volume trends, coverage spikes, and historical data delivered to your AI assistant."
canonical: "https://trendsmcp.ai/news-volume-data"
---

# News media volume data for AI agents

> Track media coverage intensity for any topic over time. How much is the press covering a company, trend, or event? News volume data tells you whether attention is building, peaking, or fading.

**Full page with live demo:** [https://trendsmcp.ai/news-volume-data](https://trendsmcp.ai/news-volume-data)

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
get_growth(keyword='artificial intelligence regulation', source='news volume', percent_growth=['6M', '1Y'])
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

### What is news volume data?

A normalized signal representing how much news coverage a topic is receiving over time. High volume means lots of articles; low volume means the topic has dropped out of media attention.

### How does news volume differ from news sentiment?

Volume measures quantity of coverage. Sentiment measures tone. A company can have high news volume with negative sentiment (a crisis) or low volume with positive sentiment (quiet steady growth). Both signals together give a fuller picture.

### Can I detect media attention spikes in real time?

Yes. Use get_top_trends with source='news' to see what is spiking in news coverage right now, without specifying a keyword.

---

## Related

- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/news-volume-data](https://trendsmcp.ai/news-volume-data)*