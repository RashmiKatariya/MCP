from mcp.server import tool

@tool()
def read_file(path: str) -> str:
    """Read file content"""
    with open(path, "r") as f:
        return f.read()

@tool()
def write_file(path: str, content: str) -> str:
    """Write to file"""
    with open(path, "w") as f:
        f.write(content)
    return "File written successfully"