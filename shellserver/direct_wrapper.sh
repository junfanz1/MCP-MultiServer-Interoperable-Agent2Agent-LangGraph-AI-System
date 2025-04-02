#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Use absolute paths to everything to avoid PATH issues
VENV_DIR="/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/shellserver/.venv"
PYTHON_BIN="$VENV_DIR/bin/python"
SERVER_DIR="/Users/junfanzhu/Desktop/MCP-AI-Infra-Real-Time-Agent/shellserver"
SERVER_SCRIPT="$SERVER_DIR/direct_server.py"

echo "Starting server with:"
echo "Python binary: $PYTHON_BIN"
echo "Server script: $SERVER_SCRIPT"

# Execute the direct server script with the explicit Python binary
cd "$SERVER_DIR"
"$PYTHON_BIN" -u "$SERVER_SCRIPT"

# If we get here, something went wrong
echo "Server exited unexpectedly" 