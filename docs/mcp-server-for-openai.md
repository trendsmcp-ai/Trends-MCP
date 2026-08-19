---
title: "Trends MCP for OpenAI - Live Trend Data via OpenAI MCP | Trends MCP"
description: "Connect Trends MCP to OpenAI's MCP-compatible tools. Give GPT-4o and o3 live trend data from Google, TikTok, Reddit, YouTube. Setup guide for OpenAI MCP integration."
canonical: "https://trendsmcp.ai/mcp-server-for-openai"
---

# Trends MCP for OpenAI

> OpenAI adopted the Model Context Protocol standard, making Trends MCP compatible with any tool built on the OpenAI API. Connect once and any GPT-4o or o3 powered application gains access to live trend data across Google, TikTok, YouTube, Reddit, Amazon, and 8 more sources.

**Full page with live demo:** [https://trendsmcp.ai/mcp-server-for-openai](https://trendsmcp.ai/mcp-server-for-openai)

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
get_growth(keyword='GPT-5', source='google search, reddit', percent_growth=['3M'])
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

### Does OpenAI support MCP?

Yes. OpenAI adopted the Model Context Protocol standard. Any application built on the OpenAI API with tool-use support can connect to remote MCP servers like Trends MCP. OpenAI's Agents SDK and Responses API both support MCP natively.

### Can I use Trends MCP with GPT-4o and o3?

Yes. When Trends MCP is connected via an MCP-compatible OpenAI integration, GPT-4o and o3 can call all Trends MCP tools as function calls. This gives the model live trend awareness beyond its training data.

### How do developers connect Trends MCP to an OpenAI-powered app?

Using the OpenAI Agents SDK, add Trends MCP as an MCPServerHTTP resource with the URL https://api.trendsmcp.ai/v1/mcp. The SDK handles tool discovery and call routing automatically.

### What is the difference between Trends MCP and OpenAI's web search tool?

OpenAI's web search tool retrieves live web pages. Trends MCP provides structured, normalized trend signals from 12+ platforms -- search volume, hashtag growth, discussion volume, web traffic -- returned as clean data that models can reason over, not raw HTML to parse.

---

## Related

- [mcp-server-for-claude](https://trendsmcp.ai/mcp-server-for-claude)
- [mcp-server-for-chatgpt](https://trendsmcp.ai/mcp-server-for-chatgpt)
- [data-sources](https://trendsmcp.ai/data-sources)

---

*Part of [Trends MCP](https://trendsmcp.ai/) &mdash; the MCP server for live trend data.*  
*Full page with structured data and live demo: [https://trendsmcp.ai/mcp-server-for-openai](https://trendsmcp.ai/mcp-server-for-openai)*