import asyncio
from fastmcp import Client

# client = Client("https://circular-orange-caribou.fastmcp.app/mcp")
client = Client("http://localhost:8001/mcp")

print("Client initialized.")

async def call_tool(name: str):
    async with client:
        print(f"Listing tools:")
        tools = await client.list_tools()
        print(tools)
        
        print(f"\nCalling tool 'greet' with name='{name}':")
        result = await client.call_tool("greet", {"name": name})
        print(result)
        
        print("\nListing resources:")
        resources = await client.list_resources()
        print(resources)
        
        print("\nCalling resource 'data://app-status':")
        resource_result = await client.read_resource("data://app-status")
        print(resource_result)
        
        print(f"\nListing prompts:")
        prompts = await client.list_prompts()
        print(prompts)
        
        print(f"\nCalling prompt 'ask_about_topic' with topic='{name}':")
        prompt_result = await client.get_prompt("ask_about_topic", {"topic": name})
        print(prompt_result)

asyncio.run(call_tool("Ford"))