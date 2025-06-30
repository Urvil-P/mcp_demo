import asyncio
from typing import Optional, Any
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def Call_Tool(self, tool_name: str, **kwargs) -> Any:
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
        await client.connect_to_server("server.py")
        if client.session:
            # result = await client.call_tool("Greet", name="Urvil")
            result = await client.Call_Tool("Greet", name="Urvil")
            print(f"[{result.content[0].text}", flush=True)

    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())