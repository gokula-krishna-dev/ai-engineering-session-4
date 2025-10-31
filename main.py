from fastmcp import FastMCP

mcp = FastMCP(name="Your MCP server name",
    instructions="This MCP server hosts tools, resources, and prompts for demonstration purposes",
    website_url="https://gokulakrishna.co",
    version="1.0.0"
)

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.resource(
    uri="data://app-status",
    name="ApplicationStatus",
    description="Provides the current status of the application.",
    mime_type="application/json",
    tags={"monitoring", "status"},
    meta={"version": "2.1", "team": "infrastructure"}
)
def get_application_status() -> dict:
    """Internal function description (ignored if description is provided above)."""
    return {"status": "ok", "uptime": 12345} 

@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

if __name__ == "__main__":
    mcp.run()