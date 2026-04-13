from mcp.client import Client

client = Client("http://localhost:8000")

print(client.call_tool("add", {"a": 10, "b": 5}))
print(client.call_tool("get_weather", {"city": "Bangalore"}))