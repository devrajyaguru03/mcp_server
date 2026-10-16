import random

from fastmcp import FastMCP

# ── Create the MCP server ────────────────────────────────────────────────────
mcp = FastMCP(
    name="Demo MCP Server",
    instructions="A simple MCP server with math and utility tools.",
)


# ── Tool 1: Sum of two numbers ───────────────────────────────────────────────
@mcp.tool()
def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: First number.
        b: Second number.
    """
    return a + b


# ── Tool 2: Generate a random number between 1 and 100 ───────────────────────
@mcp.tool()
def generate_random_number() -> int:
    """Generate and return a random integer between 1 and 100 (inclusive)."""
    return random.randint(1, 100)


# ── Resource: Server & tool information ──────────────────────────────────────
@mcp.resource("info://server")
def server_info() -> str:
    """Static information about this MCP server and the tools it exposes."""
    return """
=============================================================
  Demo MCP Server  —  Server Information
=============================================================

DESCRIPTION
  A lightweight MCP server built with FastMCP that exposes
  two utility tools for quick calculations and random-number
  generation.

TOOLS
  1. add(a, b)
     - Accepts two numbers (integers or floats).
     - Returns their sum.
     - Example: add(3.5, 2) -> 5.5

  2. generate_random_number()
     - Takes no arguments.
     - Returns a random integer in the range [1, 100].
     - Example: generate_random_number() -> 42

RESOURCES
  - info://server  - This document (server & tool overview).

TRANSPORT
  Default: stdio  (run with `uv run main.py`)
  SSE:     set transport="sse" in mcp.run() for HTTP streaming.

AUTHOR
  Dev Rajyaguru <devrajyaguru03@gmail.com>
=============================================================
""".strip()


# ── Entry point ───────────────────────────────────────────────────────────────
# Default transport is stdio — required for MCP Inspector and most MCP clients.
# To run as an HTTP server instead, use:  mcp.run(transport="http", port=8000)
if __name__ == "__main__":
    try:
        mcp.run()  # stdio transport (auto-detected by MCP clients)
    except KeyboardInterrupt:
        pass  # Ctrl+C is normal — suppress the ugly traceback
