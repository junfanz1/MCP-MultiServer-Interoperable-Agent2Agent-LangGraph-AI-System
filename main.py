import asyncio
import os

from dotenv import load_dotenv

load_dotenv()
#print(os.getenv("OPENAI_API_KEY"))
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

"""
load_mcp_tools: taking the tools which are exposed through MCP server and are an MCP object, and to transform it into a LangChain tool. So we can use in LangChain or LangGraph agent.
ClientSession: provides framework for Python app to act as MCP client. It's responsible to connect to MCP server to exchange messages, react to server requests and notifications through customizable callbacks. It's initialize method can make request to server to establish connection parameters according to MCP specification.
StdioServerParameters: Pydantic class which has fields of commands and args, which represent how the client to run MCP server, whether with Python, Node or Docker, etc.
stdio_client: client communicate with MCP server through transport of input and output. Read from standard in, and write to standard out.
"""

llm = ChatOpenAI()

# initialize variables and give info of how to run MCP server
stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/servers/math_server.py"],
)

async def main():
    # context manager, every client connect to server via a session
    async with stdio_client(stdio_server_params) as (read, write):
        # feed session with read and write
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize() # client initialize connection with MCP server
            print("session initialized")
            # MCP server respond with available tools/resources to client
            tools = await session.list_tools()
            print(tools)
            # create host application (LangGraph ReAct agent) containing client info
            tools = await load_mcp_tools(session)
            print(tools)
            agent = create_react_agent(llm, tools)
            result = await agent.invoke({"messages": [HumanMessage(content="What's 1+1?")]})
            print(result["messages"][-1].content)

"""
Motivation of combining LangGraph, LangChain and MCP:
LangGraph agent, with help of MCP client, is making request to MCP server, and execution of tool is in server side, which is decoupled from LangGraph application.
LangGraph app is responsible for orchestration, MCP server is responsible for execution of tools.
"""



if __name__ == "__main__":
    asyncio.run(main())
