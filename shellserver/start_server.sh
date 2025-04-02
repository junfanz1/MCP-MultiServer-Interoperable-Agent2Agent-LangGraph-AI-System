#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Go to the correct directory
cd /Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/shellserver
echo "Changed to directory: $(pwd)"

# Activate the virtual environment
source .venv/bin/activate
echo "Activated virtual environment"

# Check if mcp is installed
if pip list | grep -q mcp; then
    echo "MCP is installed: $(pip show mcp | grep Version)"
else
    echo "Error: MCP is not installed in this environment"
    exit 1
fi

# Run the server with explicit output
echo "Starting server.py directly using Python..."
python -u server.py  # -u for unbuffered output

# If we get here, something went wrong as the server should keep running
echo "Server exited unexpectedly" 