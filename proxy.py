from fastmcp import FastMCP

# Target a remote SSE server directly by URL
proxy = FastMCP.as_proxy("http://localhost:8000/mcp", name="Streamable HTTP to Stdio Proxy")

proxy
# Start the proxy
if __name__ == "__main__":
    proxy.run()
