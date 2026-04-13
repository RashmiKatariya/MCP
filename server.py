from mcp.server import Server

app = Server("ai-agent-mcp-server")

# Register tools
import tools.math_tools
import tools.file_tools
import tools.api_tools

if __name__ == "__main__":
    app.run()