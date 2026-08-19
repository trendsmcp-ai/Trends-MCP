---
title: "Developer Ecosystem Trends for AI via MCP - npm, GitHub, App Data | Trends MCP"
description: "Track developer ecosystem trends via MCP. npm weekly downloads, app download growth, Steam player counts, and web traffic -- all queryable by your AI. No API keys."
canonical: "https://trendsmcp.ai/developer-ecosystem-trends"
---

# Developer ecosystem trends for AI agents

> npm weekly downloads, mobile app install growth, and web traffic trends are the clearest signals of developer and user adoption. Trends MCP delivers all of them to your AI in one query -- useful for technology due diligence, framework selection, and developer market research.

**Full page with live demo:** [https://trendsmcp.ai/developer-ecosystem-trends](https://trendsmcp.ai/developer-ecosystem-trends)

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
get_growth(keyword='@anthropic-ai/sdk', source='npm', percent_growth=['1M', '3M', '6M'])
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

### What developer signals does Trends MCP provide?

npm weekly download counts (library and framework adoption velocity), Android app install trends via Google Play (mobile user acquisition growth), Steam concurrent player counts (gaming platform engagement), and web traffic trends for developer tools and SaaS products. All normalized and queryable via MCP.

### How is npm download data useful for investment or technology research?

npm downloads are a leading indicator of developer ecosystem adoption. A library growing consistently in weekly downloads is gaining mindshare before its commercial success is publicly visible. Investors and technology analysts use npm trends to validate whether a developer platform or toolchain is actually gaining traction.

### Can I compare multiple npm packages side by side?

Yes. Call get_growth for each package name and compare the growth rates. Common comparisons: React vs Vue vs Svelte, OpenAI SDK vs Anthropic SDK, Tailwind vs Bootstrap.

### Can I track a mobile app's growth without an app store developer account?

Yes. Trends MCP accesses Google Play install trend data via AppBrain estimates. Query by Android bundle ID (e.g. 'com.openai.chatgpt') and get normalized install trend data and growth rates without any app store credentials.

---

## Related

- [npm-trends](https://trendsmcp.ai/npm-trends)
- [app-download-trends](https://trendsmcp.ai/app-download-trends)
- [steam-trends](https://trendsmcp.ai/steam-trends)
- [web-traffic-data](https://trendsmcp.ai/web-traffic-data)
- [investment-research](https://trendsmcp.ai/investment-research)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/developer-ecosystem-trends](https://trendsmcp.ai/developer-ecosystem-trends)*