from mcp.server.fastmcp import FastMCP
import sys

# Create the server instance
mcp = FastMCP("Simple Demo", host="0.0.0.0", port=8000)

# Add a simple tool
@mcp.tool()
def Greet(name: str) -> str:
    """Greet a person."""
    print(f"[Server] Received name: {name}", flush=True)
    return f"Hello, {name}!"

@mcp.tool()
def Good_Greet(name:str) -> str:
    """Good Greet a person."""
    print(f"[Server] Received name: {name}", flush=True)
    return f"Jai Sri Ram, {name}!"

# Start the server
if __name__ == "__main__":
    # Default transport
    transport = "stdio"

    # Only ask for input if running interactively
    if sys.stdin.isatty():
        print("1 for sse")
        print("2 for streamable-http")
        choice = input("Enter the transport type (default: stdio): ").strip()
        print(f"choice: {choice}")

        if choice == "1":
            transport = "sse"
        elif choice == "2":
            transport = "streamable-http"

    print(f"Using transport: {transport}")
    mcp.run(transport=transport)
