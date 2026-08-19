---
title: "AI Social Listening - Real-Time Social Monitoring via MCP | Trends MCP"
description: "Social listening for AI assistants via MCP. Monitor brand mentions, track topic conversations, and measure social sentiment across Reddit, Twitter, TikTok, YouTube, and News in real time."
canonical: "https://trendsmcp.ai/social-listening-ai"
---

# AI-powered social listening via MCP

> Traditional social listening tools are dashboards you have to check manually. Trends MCP brings social monitoring into your AI assistant: ask Claude or Cursor to track brand mentions, measure sentiment trends, or identify emerging conversations -- and get structured answers from Reddit, Twitter, TikTok, YouTube, and News in one call.

**Full page with live demo:** [https://trendsmcp.ai/social-listening-ai](https://trendsmcp.ai/social-listening-ai)

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
get_growth(keyword='your brand', source='reddit, news sentiment, twitter', percent_growth=['1M', '3M'])
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

### What platforms does AI social listening via MCP cover?

Reddit (community discussion volume), Twitter/X (mention trends), TikTok (hashtag and video trends), YouTube (comment and search trends), LinkedIn (professional discussion), and News (thousands of outlets via sentiment analysis). All in one query.

### How is this different from Brandwatch or Mention?

Brandwatch and Mention are dedicated dashboards you check periodically. Trends MCP puts social listening directly inside your AI assistant, so you can ask natural language questions like 'Is brand X getting more negative press this month?' and get a structured answer immediately -- no dashboard to log into.

### Can I track sentiment, not just volume?

Yes. The News Sentiment source returns positive/negative/neutral scores for any topic alongside volume. Reddit and Twitter data includes discussion velocity signals that correlate with sentiment shifts.

### Is this useful for PR crisis monitoring?

Yes. Set up regular checks using get_growth for a brand name with source='news sentiment, reddit, twitter' to detect unusual spikes in negative coverage or discussion volume before they become a full crisis.

---

## Related

- [brand-monitoring](https://trendsmcp.ai/brand-monitoring)
- [reddit-trends](https://trendsmcp.ai/reddit-trends)
- [twitter-trends](https://trendsmcp.ai/twitter-trends)
- [news-sentiment-data](https://trendsmcp.ai/news-sentiment-data)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/social-listening-ai](https://trendsmcp.ai/social-listening-ai)*