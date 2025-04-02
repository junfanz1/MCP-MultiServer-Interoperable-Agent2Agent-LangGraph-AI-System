# MCP Terminal Command Server

A simple MCP (Model Context Protocol) server that exposes a tool for running terminal commands.

## Overview

This server provides a single tool:

- `run_terminal_command`: Executes a terminal command and returns the output, exit code, and success status.

## Installation

### Prerequisites

- Python 3.7+
- MCP Python SDK: `pip install mcp`

### Running the Server

There are three ways to run the server:

1. Run with the MCP Inspector (for testing and development):
   ```
   mcp dev server.py
   ```

2. Run the server directly:
   ```
   mcp run server.py
   ```

3. Install the server in Claude Desktop:
   ```
   mcp install server.py
   ```

## Using the Terminal Command Tool

The `run_terminal_command` tool accepts a single argument:

- `command`: The terminal command to execute (as a string)

The tool returns a dictionary with the following fields:

- `output`: Combined stdout and stderr output from the command
- `exit_code`: The exit code returned by the command (0 typically means success)
- `success`: Boolean indicating if the command executed successfully (exit_code == 0)

## Security Considerations

⚠️ **Warning**: This tool executes terminal commands directly on your system. Use with caution and only with trusted inputs.

## Example Usage

When connected to Claude Desktop, you can ask the LLM to run terminal commands:

```
Could you please list the files in my current directory?
```

Claude will use the `run_terminal_command` tool to execute `ls -la` and return the output.

## License

MIT
