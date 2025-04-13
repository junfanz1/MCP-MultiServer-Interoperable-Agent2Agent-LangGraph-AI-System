"""
LangChain MultiServer MCP Client

1-1 connection between client and MCP server, inside LangChain we have multiple MCP clients to easily connect to multiple MCP servers.
"""
import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()

async def main():
    async with MultiServerMCPClient({"math":{"command": "python", "args": ["/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/servers/math_server.py"]},
                                    "weather":{"url":"http://localhost:8000/sse", "transport":"sse"}
                                     }) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke({"message":"what's 1+1?"})
        print(result["message"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())


