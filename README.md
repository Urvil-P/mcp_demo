# MCP Transport Mechanisms Demo

A comprehensive demonstration of Model Context Protocol (MCP) server implementation with three different transport mechanisms: **stdio**, **SSE**, and **streamable-http**.

## 🚀 Overview

This repository showcases how to implement and use MCP servers with different transport layers, each optimized for specific use cases:

- **stdio**: Perfect for local development and testing
- **SSE (Server-Sent Events)**: Ideal for remote MCP servers
- **streamable-http**: Best for remote MCP servers with enhanced streaming capabilities

## 📁 Project Structure

```
├── server.py              # MCP server implementation
├── stdio_client.py        # Client for stdio transport
├── sse_client.py          # Client for SSE transport
├── streamable_http_client.py # Client for streamable-http transport
├── pyproject.toml         # UV package configuration
└── README.md             # This file
```

## 🛠 Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Urvil-P/mcp_demo.git
cd mcp-demo
```

2. Install dependencies using uv:
```bash
uv sync
```

## 🎯 Transport Mechanisms

### 1. stdio Transport
**Use Case**: Local development and testing

**Features**:
- Direct process communication
- No network overhead
- Simple debugging
- Perfect for development workflows

**Usage**:
```bash
# No server startup required - client manages the server process
uv run stdio_client.py
```

### 2. SSE (Server-Sent Events) Transport
**Use Case**: Remote MCP servers

**Features**:
- Real-time server-to-client communication
- Built on HTTP/1.1
- Automatic reconnection support
- Ideal for live data streaming

**Usage**:
```bash
# Terminal 1: Start the server
uv run server.py

# Terminal 2: Run the SSE client
uv run sse_client.py
```

### 3. Streamable-HTTP Transport
**Use Case**: Remote MCP servers with enhanced streaming

**Features**:
- Optimized for high-performance streaming
- Better resource utilization
- Enhanced scalability
- Modern HTTP streaming capabilities

**Usage**:
```bash
# Terminal 1: Start the server
uv run server.py

# Terminal 2: Run the streamable-http client
uv run streamable_http_client.py
```

## 🔄 Testing the Implementation

### stdio Transport
```bash
uv run stdio_client.py
```
*Note: The stdio transport doesn't require a separate server process as it manages the server lifecycle internally.*

### SSE and Streamable-HTTP Transports
For both SSE and streamable-http transports, you need to start the server first:

1. **Start the server**:
```bash
uv run server.py
```

2. **Test SSE transport**:
```bash
uv run sse_client.py
```

3. **Test streamable-http transport**:
```bash
uv run streamable_http_client.py
```

## 📚 Learning More

For a detailed comparison between SSE and streamable-http transports, check out this informative video:

[![SSE vs Streamable-HTTP](https://img.youtube.com/vi/zfSsKOgJGlE/0.jpg)](https://youtu.be/zfSsKOgJGlE?si=IaMQqpBNryvQ_zgs)

## 🏗 Architecture

### Server (`server.py`)
The main MCP server implementation that supports all three transport mechanisms. It handles:
- Protocol negotiation
- Message routing
- Resource management
- Transport-specific adaptations

### Clients
Each client demonstrates how to connect and communicate with the MCP server using different transport mechanisms:

- **`stdio_client.py`**: Demonstrates local process communication
- **`sse_client.py`**: Shows real-time server-sent events usage
- **`streamable_http_client.py`**: Implements high-performance HTTP streaming

## 🎨 Transport Selection Guide

| Transport | Local Dev | Remote Server | Real-time | Performance | Complexity |
|-----------|-----------|---------------|-----------|-------------|------------|
| stdio | ✅ Best | ❌ No | ⚡ Fast | 🔥 Excellent | 🟢 Simple |
| SSE | ✅ Good | ✅ Yes | ⚡ Fast | 🔥 Good | 🟡 Medium |
| streamable-http | ✅ Good | ✅ Yes | ⚡ Very Fast | 🔥 Excellent | 🟡 Medium |


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Useful Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [UV Package Manager](https://docs.astral.sh/uv/)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

---

**Happy coding!** 🎉