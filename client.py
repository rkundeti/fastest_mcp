import asyncio
import json
from fastmcp import Client
from ollama import chat
from fastmcp.client.transports import StdioTransport
from ollama import chat

MODEL = "llama3.1"
MCP_URL = "http://localhost:8080/mcp"

async def main():
    transport = StdioTransport(
        command="python",
        args=["server.py"],
        cwd=r"C:\Ramana\fastest_mcp",
    )
    async with Client(transport) as mcp_client:
        tools = await mcp_client.list_tools()
        print("Connected tools:", [t.name for t in tools])

client = Client("http://127.0.0.1:8000/mcp")
##client = Client("https://mass-peach-ant.fastmcp.app/mcp")


async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool())