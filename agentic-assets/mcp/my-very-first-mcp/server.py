"""MCP server for my-very-first-mcp.

Every function decorated with ``@mcp.tool`` becomes a tool the agent can call;
the docstring is what it reads to decide when to call it. Edit freely — this
file IS the server, and it ships inside this asset.
"""

from fastmcp import FastMCP

mcp = FastMCP('my-very-first-mcp')


@mcp.tool
def hello(who: str = "world") -> str:
    """Say hello. Replace this with a tool of your own."""
    return f"hello {who}"
