---
title: "Trend Forecasting with AI - Predict Trends via MCP | Trends MCP"
description: "Use AI to forecast trends before they peak. Trends MCP gives your AI live cross-platform signals to identify emerging trends early -- across Google, TikTok, Reddit, YouTube, and more."
canonical: "https://trendsmcp.ai/trend-forecasting"
---

# Trend forecasting with AI

> The best trend forecasters catch signals before they become obvious. Trends MCP gives your AI the cross-platform data to do exactly that: detect a keyword accelerating on TikTok before it reaches Google Search, spot a Reddit discussion gaining momentum before it hits mainstream news, and identify product demand building on Amazon before it shows up in industry reports.

**Full page with live demo:** [https://trendsmcp.ai/trend-forecasting](https://trendsmcp.ai/trend-forecasting)

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
get_growth(keyword='emerging topic', source='tiktok, reddit, google search', percent_growth=['1M', '3M'])
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

### How does AI trend forecasting work with Trends MCP?

Trends MCP provides the multi-platform signal data. Your AI (Claude, ChatGPT, Cursor, etc.) can analyze growth acceleration across platforms, identify divergences (growing on TikTok but not yet on Google), and reason about which signals precede mainstream breakout. The AI does the pattern recognition; Trends MCP supplies the live data.

### Which data sources are the best leading indicators?

TikTok and Reddit typically lead Google Search by 2-6 weeks for consumer trends. GitHub and npm lead Google Search for developer trends. News volume spikes often precede Google Search peaks. Trends MCP lets you query all of these simultaneously to build a multi-signal leading indicator view.

### Can I track whether a trend is accelerating or plateauing?

Yes. Compare get_growth with different time windows (1M vs 3M vs 1Y) to identify whether a trend is in early acceleration, peak growth, or beginning to plateau.

### Who uses trend forecasting data?

Brand strategists identifying emerging categories, product teams validating new product ideas before launch, investors looking for early demand signals, content creators spotting topics before they get crowded, and market researchers building trend reports.

---

## Related

- [market-research](https://trendsmcp.ai/market-research)
- [viral-trend-detection](https://trendsmcp.ai/viral-trend-detection)
- [investment-research](https://trendsmcp.ai/investment-research)
- [real-time-trends-api](https://trendsmcp.ai/real-time-trends-api)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/trend-forecasting](https://trendsmcp.ai/trend-forecasting)*