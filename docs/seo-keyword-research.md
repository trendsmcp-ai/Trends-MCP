---
title: "AI SEO Keyword Research with Live Trend Data via MCP | Trends MCP"
description: "Give your AI live Google Search trend data for SEO keyword research. Find rising keywords, track search volume momentum, and compare competitors via MCP."
canonical: "https://trendsmcp.ai/seo-keyword-research"
---

# AI-powered SEO keyword research with live search trends

> Let your AI find the keywords worth targeting -- before your competitors do. Trends MCP gives your AI live Google Search demand data: rising queries, volume trajectory, period-over-period growth, and cross-platform signals that confirm whether search intent is accelerating or fading.

**Full page with live demo:** [https://trendsmcp.ai/seo-keyword-research](https://trendsmcp.ai/seo-keyword-research)

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
get_growth(keyword='mcp server', source='google search', percent_growth=['1M', '3M', '1Y'])
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

### How does Trends MCP help with SEO keyword research?

Your AI can: (1) compare growth trajectories for a list of candidate keywords and rank them by rising demand, (2) identify keywords growing rapidly on Google Search but still low in competition, (3) validate whether a keyword's search interest is compounding or declining before you invest in content, (4) find emerging keyword clusters by querying related terms across Google Search and Google Shopping.

### Can Trends MCP find keywords with rising search volume?

Yes. Use get_growth for a list of keywords and the API returns period-over-period growth percentages. Keywords with strong 1M and 3M growth and low absolute volume are the highest-potential early targets.

### How does this compare to Ahrefs or Semrush for keyword research?

Ahrefs and Semrush give you historical volume estimates and difficulty scores. Trends MCP gives your AI live momentum data -- which keywords are growing right now, week over week. The two are complementary: use Ahrefs/Semrush for difficulty and existing traffic data, Trends MCP for trend trajectory and cross-platform demand validation.

### Can I track cross-platform search intent?

Yes. A keyword growing on Google Shopping but not Google Search signals purchase intent outpacing information-seeking -- a strong signal for e-commerce content. Comparing YouTube and Google Search reveals content format preferences for the same topic.

---

## Related

- [content-strategy](https://trendsmcp.ai/content-strategy)
- [google-trends](https://trendsmcp.ai/google-trends)
- [google-search-trends](https://trendsmcp.ai/google-search-trends)
- [google-shopping-trends](https://trendsmcp.ai/google-shopping-trends)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/seo-keyword-research](https://trendsmcp.ai/seo-keyword-research)*