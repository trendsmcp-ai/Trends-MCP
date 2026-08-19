---
title: "AI Market Research with Live Trend Data via MCP | Trends MCP"
description: "Give your AI live market trend data for research. Query consumer demand, cross-platform signals, and competitor activity across Google, TikTok, Reddit, Amazon, and more via MCP."
canonical: "https://trendsmcp.ai/market-research"
---

# AI-powered market research with live trend data

> Stop copy-pasting from Google Trends into your AI. Connect Trends MCP and your AI assistant can pull consumer demand signals, cross-platform trend momentum, and competitive intelligence directly -- across Google, TikTok, YouTube, Reddit, Amazon, Wikipedia, and news in one session.

**Full page with live demo:** [https://trendsmcp.ai/market-research](https://trendsmcp.ai/market-research)

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
get_growth(keyword='collagen supplements', source='all', percent_growth=['3M', '1Y'])
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

### What market research workflows does Trends MCP support?

Category sizing (how big and growing is demand for a product or topic), competitive analysis (comparing search momentum for competing brands or products), consumer demand validation (is interest rising or falling), trend forecasting (5-year historical trajectory to project future demand), and channel breakdown (which platforms are driving awareness).

### Can I use Trends MCP to validate a new product idea?

Yes. A typical workflow: (1) query Google Search and Amazon demand for the product category to measure consumer intent, (2) check TikTok and Reddit for community discussion growth, (3) review Wikipedia page views for information-seeking spikes, (4) compare against competitor brand search trends. Your AI assembles all of this in one session.

### How does Trends MCP compare to traditional market research tools?

Traditional tools give you reports. Trends MCP gives your AI live data it can reason over, synthesize, and present in any format you need -- a table, a summary, a competitive ranking -- without you leaving your AI conversation or exporting CSVs.

### Which data sources are most useful for market research?

Google Search (consumer intent at scale), Amazon (purchase intent specifically), TikTok (early-stage viral demand), Reddit (community and enthusiast interest), News Sentiment (media attention and tone), Wikipedia (information-seeking spikes), and Web Traffic (competitor site visit trends).

---

## Related

- [competitor-tracking](https://trendsmcp.ai/competitor-tracking)
- [brand-monitoring](https://trendsmcp.ai/brand-monitoring)
- [google-trends](https://trendsmcp.ai/google-trends)
- [amazon-search-trends](https://trendsmcp.ai/amazon-search-trends)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/market-research](https://trendsmcp.ai/market-research)*