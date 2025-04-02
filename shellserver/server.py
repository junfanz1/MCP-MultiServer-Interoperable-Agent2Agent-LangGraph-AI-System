#!/usr/bin/env python3
"""
Simple MCP Server with Terminal Command Tool
"""

import subprocess
from typing import Dict, Any
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Create an MCP server with a standard name
mcp = FastMCP("Shell")

@mcp.tool()
def run_terminal_command(command: str) -> Dict[str, Any]:
    """
    Run a terminal command and return the output.
    
    Args:
        command: The terminal command to execute
        
    Returns:
        A dictionary containing the command output and exit code
    """
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

@mcp.resource("file:///readme")
def get_readme() -> str:
    """
    Expose the mcpreadme.md file from the user's Desktop directory.
    
    Returns:
        The contents of the mcpreadme.md file as a string.
    """
    # Get the path to the user's Desktop directory
    desktop_path = Path.home() / "Desktop"
    readme_path = desktop_path / "mcpreadme.md"
    
    # Check if the file exists
    if not readme_path.exists():
        return "Error: mcpreadme.md file not found on Desktop."
    
    # Read and return the file contents
    try:
        return readme_path.read_text()
    except Exception as e:
        return f"Error reading mcpreadme.md: {str(e)}"

# Simple entry point to run the server
if __name__ == "__main__":
    print("Starting MCP Shell server...")
    mcp.run()
