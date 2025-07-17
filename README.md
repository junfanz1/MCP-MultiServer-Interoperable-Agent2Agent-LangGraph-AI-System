[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/junfanz1-mcp-multiserver-interoperable-agent2agent-langgraph-ai-system-badge.png)](https://mseep.ai/app/junfanz1-mcp-multiserver-interoperable-agent2agent-langgraph-ai-system)

# Part 1. Real-Time LangGraph Agent with MCP Tool Execution

This project demonstrates a decoupled real-time agent architecture that connects [LangGraph](https://github.com/langchain-ai/langgraph) agents to remote tools served by custom MCP (Modular Command Protocol) servers. The architecture enables a flexible and scalable multi-agent system where each tool can be hosted independently (via SSE or STDIO), offering modularity and cloud-deployable execution.

- **Decoupled Architecture:** Engineered a modular system where LangGraph-based agents orchestrate LLM workflows while delegating tool execution to remote MCP servers via both SSE and STDIO transports.
- **Advanced Asynchronous Programming:** Utilized Python’s async/await for non-blocking I/O, ensuring concurrent execution of multiple tools and scalable real-time communication.
- **MCP & LangGraph Integration:** Demonstrated deep expertise in integrating Modular Command Protocol (MCP) with LangGraph and LangChain, enabling seamless transformation and invocation of distributed tools.
- **Flexible Multi-Server Connectivity:** Designed a MultiServerMCPClient that supports 1:1 bindings to various tool servers, highlighting the system’s ability to integrate diverse environments (local, cloud, containerized).
- **Robust Agent-to-Tool Communication:** Implemented detailed client sessions, handshake protocols, and dynamic tool discovery, ensuring reliable execution and interaction between agents and MCP servers.
- **Forward-Looking Interoperability:** Laid the groundwork for an Agent2Agent protocol, aiming for an ecosystem where AI agents can share capabilities, coordinate actions, and securely exchange context and data.


---

## 🚀 Project Purpose

This project aims to:

- Decouple **LLM-based agent orchestration** (LangGraph) from **tool execution** (via MCP servers).
- Enable **real-time, multi-server**, and **language-agnostic** tool integration using the MCP protocol.
- Showcase how to:
  - Spin up LangChain-compatible MCP tool servers (e.g., `math_server.py`, `weather_server.py`)
  - Integrate them with LangGraph ReAct agents
  - Use **async/await** programming for non-blocking I/O across agents and tool servers

---

## 📦 Project Structure

```bash
.
├── servers/
│   ├── math_server.py         # STDIO-based MCP tool server
│   └── weather_server.py      # SSE-based MCP tool server
├── client/
│   ├── multiserver_client.py  # LangGraph agent using MultiServer MCP client
│   └── stdio_client.py        # LangGraph agent using STDIO transport
```


---

## 🔧 Technology Stack

- 🧠 **LangGraph**: ReAct agent orchestration
- 🔗 **LangChain**: LLM pipeline & tools abstraction
- 🧰 **MCP (Modular Command Protocol)**:
  - `FastMCP` – FastAPI-based server abstraction
  - `ClientSession`, `StdioServerParameters`, `MultiServerMCPClient`
- 🌐 **SSE** & **STDIO**: Transport protocols
- 🔁 **AsyncIO**: Asynchronous concurrency
- ☁️ **OpenAI**: Backend LLM (via `langchain_openai`)
- 🧪 **dotenv**: API key management

---

## 📜 Source Code Breakdown

### 1. `math_server.py` and `weather_server.py`

Tool servers using `FastMCP`:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    return "Cold in Chicago"

if __name__ == "__main__":
    mcp.run(transport="sse")
```

✅ Highlights:
- Each server defines an async tool via @mcp.tool()
- Server is transport-agnostic: can run over SSE or STDIO
- Designed for modular deployment: local, cloud, containerized

### 2. `multiserver_client.py`

Agent that talks to multiple MCP servers concurrently:

```py
async with MultiServerMCPClient({
    "math": {"command": "python", "args": ["math_server.py"]},
    "weather": {"url": "http://localhost:8000/sse", "transport": "sse"}
}) as client:
    agent = create_react_agent(llm, client.get_tools())
    result = await agent.ainvoke({"message":"what's 1+1?"})
```

✅ Highlights:
- MultiServerMCPClient supports 1:1 bindings to multiple servers
- All tool invocations are async + streamed via appropriate transport
- Tools auto-transformed to LangChain-compatible format

### 3. `stdio_client.py`

Agent connects to one STDIO MCP server using raw ClientSession:

```py
async with stdio_client(StdioServerParameters(...)) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await load_mcp_tools(session)
        agent = create_react_agent(llm, tools)
        result = await agent.invoke({"messages": [HumanMessage(content="What's 1+1?")]})
```

✅ Highlights:
- `ClientSession.initialize()` sets up MCP spec-compliant handshake
- Tools dynamically discovered via `session.list_tools()` and `load_mcp_tools()`
- Shows low-level control over I/O streams

## 🔄 How LangGraph & MCP Interact

### Agent Flow:
1. **Agent creation** with tools from MCP client
2. Agent receives **user query**
3. Agent identifies required tool
4. MCP client sends **tool invocation request** to remote server
5. Remote server executes tool, sends result back
6. Agent consumes result and returns final response

### Architecture Diagram:

```bash
+----------------+         +----------------------+        +------------------------+
| LangGraph App  |<------->| MultiServerMCPClient |<-----> |   Remote MCP Servers   |
| (ReAct Agent)  |         |  (Tool Wrapper Layer)|        | (math_server, weather) |
+----------------+         +----------------------+        +------------------------+
                                 |                                ^
                                 |                                |
                                 +--------------------------------+
                                       Async I/O (SSE or STDIO)
```

---

## 🧠 Async Usage & Benefits

The entire system uses `async/await` to:

- Avoid blocking while waiting on tool responses
- Allow concurrent execution of multiple tools
- Enable **scalable**, real-time tool orchestration

All I/O – whether network-based (SSE) or pipe-based (STDIO) – is handled **asynchronously**, maximizing responsiveness and throughput.

---

## ✅ Pros

- **Modular & Scalable**: Tool servers can scale independently
- **Language-Agnostic**: MCP spec supports Python, Node.js, Dockerized services
- **Real-Time Execution**: SSE & STDIO transports enable live interaction
- **LangChain Compatible**: Full support for LangChain & LangGraph workflows

---

## ⚠️ Challenges

- **Tool Discovery Latency**: Initial handshake adds slight overhead
- **Transport Complexity**: Managing multiple transport types (SSE vs STDIO) can be non-trivial
- **Error Handling**: Tool server failures or timeouts must be gracefully handled
- **Deployment Strategy**: Needs orchestration layer (e.g. Docker Compose, K8s) in production

---

## 🔮 Future Directions

- **Dockerized Tool Servers** with `StdioServerParameters` + container support
- **Auth Layer** for secure server access
- **Observability**: Logs, tracing, and real-time dashboard for tool usage
- **LangGraph Parallel Nodes**: Run multiple MCP calls in parallel subgraphs
- **Multi-modal Tooling**: Extend MCP tools to support image/audio inputs

---

## 🧩 Related Concepts

- **MCP**: Protocol for defining and invoking modular tools
- **LangGraph**: State-machine inspired framework for agentic reasoning
- **ReAct**: Reasoning and Acting paradigm for structured decision-making
- **LangChain Tooling**: Converts external functions/APIs to LLM-callable tools

---

## 📌 Conclusion

This project showcases a clean separation of concerns in LLM application development:

- **LangGraph** focuses on agent logic and orchestration
- **MCP servers** handle actual task execution
- **Async clients** bridge the two, providing real-time communication

> It's a future-proof architecture for building enterprise-grade LLM applications with modular, observable, and maintainable components.

![image](https://github.com/user-attachments/assets/dd346140-d392-4b7a-9e8b-e1c485f00cd2)

## ✨ Agent2Agent Protocol

AI agents often isolated within specific applications or platforms, they lack common way to communicate, share info, or coordinate actions with other agents built by different vendors or using different frameworks. A2A defines standard way for agents to discover capabilities, agents can advertise their functions, so other agents know what they can do. Agents can assign and track tasks, including complex long running ones, exchanging status updates and results. Agents can securely exchange messages containing context instructions or data. Agents can agree on best format for presenting info (text, image) based on user interface capabilities. We aim to create interoperable ecosystem where AI agents can seamlessly work together across different enterprise applications.

![image](https://github.com/user-attachments/assets/04af2bc0-a468-4c86-a096-f856f582dcf4)


---

# Part 2. **MCP-AI-Infra-Real-Time-Agent**  

Developed an MCP-based AI infrastructure enabling real-time tool execution, structured knowledge retrieval, and dynamic agentic interactions for AI clients like Claude and Cursor.

- Designed and implemented an MCP-based AI system enabling real-time tool execution, structured knowledge retrieval, and agentic workflows for AI clients like Claude and Cursor.
- Developed an MCP server-client architecture to facilitate seamless LLM interactions, exposing tools (get_forecast, get_alerts), resources (API responses, file contents), and prompts (structured task templates).
- Engineered a dynamic tool execution framework, allowing AI models to invoke external API services with user approval, improving AI-assisted decision-making and automation.
- Integrated MCP with LangGraph-powered retrieval-augmented generation (RAG) workflows, optimizing contextual document retrieval and structured response generation.
- Implemented composable AI agents by designing an MCP protocol where AI components act as both clients and servers, enabling multi-layer agentic interactions and modular extensibility.
- Enhanced system interoperability by leveraging the MCP protocol as a universal AI interface, allowing plug-and-play AI capabilities across different host environments.
- Built a self-evolving tool registry API, enabling dynamic capability discovery and runtime tool registration, supporting adaptive AI workflows and evolving agentic systems.
- Optimized AI tool execution with caching and parallel request handling, improving MCP server response time and LLM inference efficiency.
- Utilized Anthropic’s MCP Inspector for interactive debugging and testing, refining AI-agent behavior and tool execution pipelines.
- Developed a scalable and extensible framework, enabling future integration of additional AI-driven utilities, automation agents, and external API services within the MCP ecosystem.

## **Project Overview**  
The **MCP-Servers** project is focused on implementing and extending an **MCP (Model-Controlled Protocol) Server** that facilitates real-time, documentation-grounded responses for AI systems like Claude and Cursor. The goal is to integrate an **MCP client-server architecture** that enables AI models to access structured knowledge and invoke specific tools dynamically.  

![image](https://github.com/user-attachments/assets/39d70aa7-8f7c-4481-ad89-2a29aff4d24f)

![image](https://github.com/user-attachments/assets/702eae1a-5cba-44e4-88f2-63f6cb843dd5)

![image](https://github.com/user-attachments/assets/904178db-da60-4b90-9fd3-a1eab81e0e37)

![image](https://github.com/user-attachments/assets/3859c09d-1bc5-4412-a3ef-316d5599cbdc)

![image](https://github.com/user-attachments/assets/c89fc674-1824-4ad4-b7c4-d08857fe5b85)

## **Core Objectives**  
### **1. MCP Client-Server Integration**  
- Implement an MCP server that connects to AI clients such as **Claude 3.7 Sonnet Desktop** and **Cursor**.  
- Use an existing MCP framework (e.g., [mcpdoc](https://github.com/langchain-ai/mcpdoc)) to avoid reinventing core functionalities.  

### **2. Extending MCP Server Capabilities**  
- Develop **custom tools** for the MCP server, particularly for fetching external data such as weather forecasts and alerts.  
- Expose these functionalities as **MCP tools** (`get_forecast`, `get_alerts`), making them available to AI clients.  

### **3. Enhancing AI Tool Execution**  
- Enable AI models to interact with the MCP server by invoking tools with user approval.  
- Ensure proper handling of resources (e.g., API responses, file contents) and prompts (pre-written templates for structured tasks).  

---

## **MCP Architecture & Workflow**  

### **1. MCP as a Universal AI Interface**  
- MCP functions as an **interoperability layer**, allowing external AI applications (Claude, Cursor, etc.) to interact with structured data sources and executable functions.  
- It follows a **USB-C-like architecture**, where an MCP server acts as an external plugin that can be connected to various AI systems.  

### **2. MCP Client-Server Roles**  
#### **MCP Client** (embedded in an AI host like Claude or Cursor)  
- **Requests tools**, queries resources, and processes prompts.  
- Acts as a bridge between the AI system and the MCP server.  

#### **MCP Server** (implemented locally)  
- **Exposes tools** (e.g., weather APIs) to be called dynamically by AI clients.  
- **Provides resources** (e.g., API responses, database queries).  
- **Handles prompts** to enable structured user interactions.  

---

## **Key Features & Future Enhancements**  

- **Agentic Composability**: The architecture allows **multi-layer agentic interactions**, where an AI agent can act as both an MCP client and server. This enables modular, specialized agents to handle different tasks.  
- **Self-Evolving AI via Registry API**: Future iterations could support **dynamic tool discovery**, where AI clients can register and discover new MCP capabilities in real time.  
- **Development & Debugging Support**: Utilize **Anthropic’s MCP Inspector** to test and debug MCP interactions interactively without requiring full deployment.  

---

## **Conclusion**  

This project builds an **MCP-driven AI infrastructure** that connects AI models with real-time structured knowledge, extends their capabilities via custom tool execution, and enhances agentic composability. The goal is to create an **adaptive, plugin-like AI system** that can integrate into multiple hosts while dynamically evolving through tool registration and runtime discoveries.  




## Appendix

- Not reinvent the wheel

![image](https://github.com/user-attachments/assets/e87c6ddc-1439-46cc-9df4-25d1cdd6cfea)

MCP is like USB-C, MCP server is like external device that can connect with AI (Claude Desktop) or cloud app. We can write functionality once, and plug into many MCP hosts. MCP client sits inside MCP hosts to 1:1 interact with MCP servers via MCP protocol. MCP clients invoke tools, queries for resources, interpolate prompts; MCP server expose tools (model-controlled: retrieve, DB update, send), resources (app-controlled: DB records, API), prompts (user-controlled: docs).

## MCP + Containerizing


Initialize project with UV, create virtual environment with UV, install dependencies (MCP [CLI]), index official MCP documentation with Cursor, update project with Cursor rules

![image](https://github.com/user-attachments/assets/a3e82563-a28f-4276-85c4-0ef77c415f6e)

![image](https://github.com/user-attachments/assets/33df5715-eb57-42ca-847a-e9e21979dd37)

![image](https://github.com/user-attachments/assets/9d567fdc-2a65-4cae-aef3-4e4562919abb)

![image](https://github.com/user-attachments/assets/668b67bc-1c03-4f96-b916-50ba4d39d6c3)

![image](https://github.com/user-attachments/assets/a4276001-60ea-4f66-bf6c-ee86b878af89)


Vibe coding
- @server.py implement a simple MCP server from @MCP . Use the Python SDK @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple
- help me expose a resource in my mcp server @MCP, again use @MCP Python SDK to write the code. I want to expose mcpreadme.md under my Desktop directory.

## Acknowledgements

[MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/)









