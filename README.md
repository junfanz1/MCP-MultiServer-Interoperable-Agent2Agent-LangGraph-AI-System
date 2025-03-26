# MCP-Servers

Fetch info with answers grounded in real-time documentation from official doc using MCP Server. For example, https://github.com/langchain-ai/mcpdoc as my resource to implement my MCP Server in local Claude.

![image](https://github.com/user-attachments/assets/39d70aa7-8f7c-4481-ad89-2a29aff4d24f)

![image](https://github.com/user-attachments/assets/702eae1a-5cba-44e4-88f2-63f6cb843dd5)

![image](https://github.com/user-attachments/assets/904178db-da60-4b90-9fd3-a1eab81e0e37)

![image](https://github.com/user-attachments/assets/3859c09d-1bc5-4412-a3ef-316d5599cbdc)

![image](https://github.com/user-attachments/assets/c89fc674-1824-4ad4-b7c4-d08857fe5b85)


## Project Goal

- Not reinvent the wheel
- connect prebuilt MCP server to client (Cursor, Claude 3.7 Sonnet desktop); Implement MCP server and client (use MCP SDK)
- add ability to MCP server to make request to get weather, and label this functionality of getting weather as a tool to provide to LLM
- implement tool executions that we want to expose to MCP clients (get_forecast, get_alerts)


## MCP Concepts

MCP
1. Resources: file-like data that can be read by clients (API response or file contents).
2. Tools: functions that can be called by LLM with user approval.
3. Prompts: pre-written templates that help users accomplish specific tasks

![image](https://github.com/user-attachments/assets/e87c6ddc-1439-46cc-9df4-25d1cdd6cfea)

MCP is like USB-C, MCP server is like external device that can connect with AI (Claude Desktop) or cloud app. We can write functionality once, and plug into many MCP hosts. MCP client sits inside MCP hosts to 1:1 interact with MCP servers via MCP protocol. MCP clients invoke tools, queries for resources, interpolate prompts; MCP server expose tools (model-controlled: retrieve, DB update, send), resources (app-controlled: DB records, API), prompts (user-controlled: docs).
- Sampling: allows MCP servers to request host AI system (Cursor) to generate a completion given to a kind of prompt.
- Composability: any agent can be both client and server, so we can have multi-layer agentic app to have specialized agent focusing on particular tasks.
- Registry API's future: self-evolving agent to discover new capabilities in runtime.
- Anthropic's MCP inspector: interactive dev tool for testing/debugging MCP servers, interact with MCP server without any installation.

## Cont'd.
