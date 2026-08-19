---
title: "Influencer & Creator Trend Research via MCP | Trends MCP"
description: "Find trending topics for content creators and influencers via MCP. Get live TikTok, YouTube, Reddit, and Google trend data in your AI to identify what to create next."
canonical: "https://trendsmcp.ai/influencer-trend-research"
---

# Influencer and creator trend research with AI

> Content creators who ride trends early get the most reach. Trends MCP gives your AI live trend data across TikTok, YouTube, Reddit, and Google -- so you can identify rising topics before they peak, find the cross-platform sweet spot, and build content strategy around real data instead of gut feeling.

**Full page with live demo:** [https://trendsmcp.ai/influencer-trend-research](https://trendsmcp.ai/influencer-trend-research)

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
get_top_trends(source='tiktok', limit=20)
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

### What trend data is most useful for content creators?

TikTok trending hashtags (what is getting views now), YouTube search volume (what people are watching), Google Search rising queries (what people are curious about), and Reddit discussions (what communities are engaged with). Trends MCP covers all four.

### How early can I catch a trend before it peaks?

TikTok trends typically lead Google Search by 2-6 weeks. Reddit discussions often precede TikTok by another week or two. By monitoring both TikTok and Reddit simultaneously via Trends MCP, creators can identify emerging content opportunities 3-8 weeks before they become obvious.

### Can I find trends specific to my niche?

Yes. Use get_top_trends or get_growth filtered to your content category. Many sources support category filtering -- technology, beauty, finance, gaming, food, etc.

### Can my AI suggest content ideas based on trend data?

Yes. Once Trends MCP is connected to your AI assistant, you can ask it to identify the fastest-growing topics in your niche this month and suggest content angles. The AI combines trend velocity data with its own knowledge to generate specific content ideas.

---

## Related

- [tiktok-trends](https://trendsmcp.ai/tiktok-trends)
- [youtube-trends](https://trendsmcp.ai/youtube-trends)
- [viral-trend-detection](https://trendsmcp.ai/viral-trend-detection)
- [content-strategy](https://trendsmcp.ai/content-strategy)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/influencer-trend-research](https://trendsmcp.ai/influencer-trend-research)*