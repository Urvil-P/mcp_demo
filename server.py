from mcp.server.fastmcp import FastMCP


# Create the server instance
mcp = FastMCP("Simple Demo",host="0.0.0.0",port=8000)

# Add a simple tool
@mcp.tool()
def Greet(name: str) -> str:
    """Greet a person."""
    print(f"[Server] Received name: {name}", flush=True)
    return f"Hello, {name}!"


# Start the server
if __name__ == "__main__":

    transport = "stdio"
    # transport = "sse"
    # transport = "streamable-http"

    if transport == "sse":
        print("Running Server with SSE")
        mcp.run(transport=transport)
    elif transport == "stdio":
        print("Running Server with stdio")
        mcp.run(transport="stdio")
    else:
        transport == "streamable-http"
        print("Running Server with Streamable HTTP")
        mcp.run(transport="streamable-http")