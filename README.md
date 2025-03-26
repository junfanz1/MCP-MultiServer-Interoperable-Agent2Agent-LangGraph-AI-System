
# **MCP-Servers: Technical Overview**  

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

## Cont'd.
