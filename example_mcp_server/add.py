"""
Coped and modified from http://python.langchain.com/docs/how_to/function_calling/"""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("adder")


@mcp.tool()
async def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
