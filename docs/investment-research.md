---
title: "AI Investment Research with Alternative Trend Data via MCP | Trends MCP"
description: "Give your AI live alternative data for investment research via MCP. Track consumer demand, web traffic growth, news sentiment, Wikipedia spikes, and Reddit activity for any company or sector."
canonical: "https://trendsmcp.ai/investment-research"
---

# AI investment research with live alternative data

> Consumer search trends, website traffic growth, news sentiment, Wikipedia page view spikes, and Reddit discussion volume are leading indicators of business performance. Trends MCP delivers all of them to your AI in real time -- no data vendor contracts, no CSV exports.

**Full page with live demo:** [https://trendsmcp.ai/investment-research](https://trendsmcp.ai/investment-research)

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
get_growth(keyword='palantir', source='google search, webtraffic, reddit, news sentiment, wikipedia', percent_growth=['3M', '1Y'])
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

### What alternative data signals does Trends MCP provide for investment research?

Web traffic trends (leading indicator of digital business revenue growth), Google Search brand interest (consumer awareness and demand trajectory), Reddit discussion volume (community and retail investor sentiment), News sentiment and volume (media coverage tone and intensity), Wikipedia page views (information-seeking spikes that often precede mainstream awareness), and Amazon/Google Shopping demand (consumer purchase intent for consumer-facing businesses).

### How can Wikipedia page views predict investment-relevant events?

Wikipedia page view spikes for a company or topic often occur 24-72 hours before the same event drives Google Search volume -- making them a leading indicator of public attention shifts. Sudden Wikipedia interest in a company can signal breaking news, regulatory events, or product launches before they reach full mainstream awareness.

### Can Trends MCP track website traffic as an investment signal?

Yes. Web traffic trends are a strong leading indicator for digital-first businesses -- consistent traffic growth ahead of earnings often correlates with revenue growth. You can compare traffic trajectories for a company against its peers in a single AI query.

### Is Trends MCP a replacement for Bloomberg or FactSet?

No -- it complements them. Bloomberg and FactSet provide financial fundamentals, filings, and price data. Trends MCP provides consumer-facing alternative signals: what people are searching for, buying, talking about, and clicking on. Together they give a more complete picture of business momentum.

---

## Related

- [competitor-tracking](https://trendsmcp.ai/competitor-tracking)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)
- [wikipedia-trends](https://trendsmcp.ai/wikipedia-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/investment-research](https://trendsmcp.ai/investment-research)*