#!/usr/bin/env python3
"""
Direct MCP Server Runner

This script is designed to directly run the MCP server without
relying on command-line tools like mcp or uvx.
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

# Print diagnostic information
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Ensure we're in the right directory
SERVER_DIR = Path('/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/shellserver')
os.chdir(SERVER_DIR)
print(f"Changed to directory: {os.getcwd()}")

# Try to import the MCP module
try:
    import mcp
    print(f"MCP found at: {mcp.__file__}")
    # Check MCP version without using __version__
    try:
        import pkg_resources
        mcp_version = pkg_resources.get_distribution("mcp").version
        print(f"MCP version: {mcp_version}")
    except Exception:
        print("Could not determine MCP version, but the module is loaded")
except ImportError:
    print("Error: MCP module not found. Make sure it's installed in this environment.")
    sys.exit(1)

# Import the server module directly
try:
    server_path = SERVER_DIR / 'server.py'
    spec = importlib.util.spec_from_file_location("server_module", server_path)
    server_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(server_module)
    
    # Access the mcp object from the imported module
    if hasattr(server_module, 'mcp'):
        mcp_server = server_module.mcp
        print("MCP server object found in the server module")
        
        # Start the server with the correct method (run, not start)
        print("Starting the MCP server...")
        mcp_server.run(transport='stdio')
    else:
        print("Error: Could not find MCP server object in the server module")
        sys.exit(1)
except Exception as e:
    print(f"Error loading server module: {e}")
    sys.exit(1) 