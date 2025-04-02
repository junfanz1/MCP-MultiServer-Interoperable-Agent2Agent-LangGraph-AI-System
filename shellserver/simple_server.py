#!/usr/bin/env python3
"""
Simple, clean MCP Server without any diagnostic output.
This script only runs the MCP server with stdio transport.
"""

import os
import sys
from pathlib import Path

# Ensure we're in the right directory
os.chdir(Path('/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/shellserver'))

# Import necessary modules
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Terminal Command Server")

# Define the terminal command tool
@mcp.tool()
def run_terminal_command(command: str):
    """
    Run a terminal command and return the output.
    
    Args:
        command: The terminal command to execute
    """
    import subprocess
    
    try:
        # Run the command and capture output
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            capture_output=True,
            text=True
        )
        
        # Return the command output and exit code
        return {
            "output": result.stdout + result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
        }
    except Exception as e:
        # Return error message if command execution fails
        return {
            "output": f"Error executing command: {str(e)}",
            "exit_code": -1,
            "success": False
        }

# Run the server - no printing, no diagnostic messages
if __name__ == "__main__":
    mcp.run(transport='stdio') 