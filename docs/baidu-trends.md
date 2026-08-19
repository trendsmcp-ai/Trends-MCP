---
title: "Baidu Trends MCP - China Search Trends for AI Assistants | Trends MCP"
description: "Query Baidu search trends from any AI assistant via MCP. Track keyword interest in China, monitor Chinese market demand signals, and compare to global search trends."
canonical: "https://trendsmcp.ai/baidu-trends"
---

# Baidu search trends for AI assistants

> Baidu is China's dominant search engine with over 600 million monthly users. Trends MCP gives your AI access to Baidu search trend data -- track keyword interest in China, monitor Chinese consumer demand signals, and compare mainland search momentum against global platforms in a single query.

**Full page with live demo:** [https://trendsmcp.ai/baidu-trends](https://trendsmcp.ai/baidu-trends)

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
get_trends(keyword='electric vehicles', source='baidu', data_mode='monthly')
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

### What Baidu trend data is available?

Normalized search interest over time (0-100 scale), growth rates, and comparative data versus other search platforms. Baidu data is particularly valuable for understanding Chinese consumer demand, brand awareness in China, and early signals for products entering the Chinese market.

### How does Baidu trends compare to Google Trends?

Baidu is the Google of China. For topics with strong China relevance -- manufacturing, tech hardware, EVs, luxury goods, gaming -- Baidu trend data often shows demand signals weeks before Western search platforms. Trends MCP lets you compare both in a single call.

### Can I combine Baidu data with other sources?

Yes. Use get_growth with multiple sources to compare a keyword's momentum on Baidu vs Google vs YouTube vs TikTok simultaneously.

### Who finds Baidu trends most useful?

Supply chain analysts tracking Chinese demand, companies entering or monitoring the Chinese market, researchers studying East-West information divergence, and investment analysts watching for China-led consumption trends.

---

## Related

- [google-trends](https://trendsmcp.ai/google-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [market-research](https://trendsmcp.ai/market-research)
- [investment-research](https://trendsmcp.ai/investment-research)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/baidu-trends](https://trendsmcp.ai/baidu-trends)*