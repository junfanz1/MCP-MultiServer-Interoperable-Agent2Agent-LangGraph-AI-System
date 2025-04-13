# math_server.py
# weather_server.py
"""
SSE server: we can deploy them everywhere we want, e.g. deploy in the enterprise cloud.
"""
from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    print("This is a log from the SSE server")
    return "Cold in Chicago"

if __name__ == "__main__":
    mcp.run(transport="sse")