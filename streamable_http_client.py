import asyncio
from typing import Optional, Any
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, server_url: str):
        """Connect to an MCP server with HTTP Streamable transport"""
        http_transport = await self.exit_stack.enter_async_context(
            streamablehttp_client(url=server_url)
        )

        read_stream, write_stream, _ = http_transport

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\n[Client] Connected to server with tools:", [tool.name for tool in tools])

    async def call_tool(self, tool_name: str, **kwargs) -> Any:
        if not self.session:
            raise RuntimeError("Client is not connected to any server")

        print(f"[Client] Calling tool: {tool_name} with args {kwargs}", flush=True)
        response = await self.session.call_tool(tool_name, kwargs)
        return response

    async def close(self):
        await self.exit_stack.aclose()
        print("[Client] Connection closed.", flush=True)


async def main():
    client = MCPClient()
    try:
        
        await client.connect_to_server("http://127.0.0.1:8000/mcp/")

        # Call your tool
        TOOL_NAME = "Greet"

        if TOOL_NAME == "Greet":
            result = await client.call_tool(TOOL_NAME,name="Urvil")
            print(result.content[0].text)


    finally:
        print()
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
