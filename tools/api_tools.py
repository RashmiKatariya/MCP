from mcp.server import tool
import requests

@tool()
def get_weather(city: str) -> str:
    """Get weather info"""
    return requests.get(f"https://wttr.in/{city}?format=3").text