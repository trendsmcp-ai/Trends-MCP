---
title: "GitHub & Developer Trends MCP - npm and Developer Data for AI | Trends MCP"
description: "Track GitHub trending repositories and npm package adoption via MCP. Developer trend data for AI assistants: package downloads, framework growth, and tech stack momentum."
canonical: "https://trendsmcp.ai/github-trends"
---

# GitHub and developer trends for AI assistants

> Which frameworks are developers actually adopting? Which npm packages are growing fastest? Trends MCP gives your AI structured developer trend data from npm downloads, cross-referenced with Google Search and Reddit discussion volume -- so you can make technology decisions backed by real adoption data, not hype.

**Full page with live demo:** [https://trendsmcp.ai/github-trends](https://trendsmcp.ai/github-trends)

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
get_growth(keyword='bun', source='npm, google search, reddit', percent_growth=['3M', '1Y'])
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

### What developer trend data does Trends MCP provide?

npm weekly package downloads (the most reliable proxy for developer adoption), cross-referenced with Google Search volume for technology terms and Reddit discussion trends for developer communities. Together these give a complete picture of technology momentum.

### How is npm data more useful than GitHub stars?

GitHub stars are a vanity metric easily inflated by marketing campaigns. npm weekly downloads represent actual production usage -- developers who have chosen a package for a real project. Trends MCP surfaces download trends and growth rates, not just raw counts.

### Can I compare multiple frameworks at once?

Yes. Use get_growth with a list of keywords to compare, for example, 'react vs vue vs svelte' across npm, Google Search, and Reddit simultaneously.

### Who uses developer trend data?

CTOs and architects making technology stack decisions, VCs tracking developer tool adoption, technical content creators identifying trending topics, and developers evaluating which libraries to build on.

---

## Related

- [npm-trends](https://trendsmcp.ai/npm-trends)
- [developer-ecosystem-trends](https://trendsmcp.ai/developer-ecosystem-trends)
- [search-trend-api](https://trendsmcp.ai/search-trend-api)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/github-trends](https://trendsmcp.ai/github-trends)*