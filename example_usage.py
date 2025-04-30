"""
Example script demonstrating how to use the Confluence MCP server.
This script uses the MCP client to connect to the server and execute operations.
"""
import asyncio
import json
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["server.py"],  # Server script
    env=None,  # Use default environment
)

async def print_json(data):
    """Print data as formatted JSON."""
    print(json.dumps(data, indent=2))

async def run_examples():
    """Run example operations against the Confluence server."""
    print("Connecting to Confluence MCP server...")
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            # List available tools
            print("\n=== Available Tools ===")
            tools = await session.list_tools()
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")
            
            # Example 1: Find pages by space
            print("\n=== Finding pages in space 'COD' ===")
            try:
                result = await session.call_tool(
                    "find_pages_by_space", 
                    arguments={"spaceKey": "COD", "limit": 5}
                )
                await print_json(result)
            except Exception as e:
                print(f"Error finding pages: {str(e)}")
            
            # Example 2: Execute CQL search
            print("\n=== Executing CQL search ===")
            try:
                result = await session.call_tool(
                    "execute_cql_search", 
                    arguments={"cql": "space = COD", "limit": 3}
                )
                await print_json(result)
            except Exception as e:
                print(f"Error executing search: {str(e)}")
            
            # Example 3: Find page by title
            print("\n=== Finding page by title ===")
            try:
                result = await session.call_tool(
                    "find_page_by_title", 
                    arguments={"title": "demo page", "spaceKey": "COD"}
                )
                await print_json(result)
                
                # If we found a page, get its content
                if result.get("results") and len(result["results"]) > 0:
                    page_id = result["results"][0]["id"]
                    
                    print(f"\n=== Getting content for page {page_id} ===")
                    content_result = await session.call_tool(
                        "get_page_with_body", 
                        arguments={"pageId": page_id}
                    )
                    
                    # Just print the title and a snippet of the body to avoid too much output
                    print(f"Title: {content_result.get('title', 'Unknown')}")
                    body = content_result.get("body", {}).get("storage", {}).get("value", "")
                    print(f"Body snippet: {body[:100]}...")
            except Exception as e:
                print(f"Error finding page: {str(e)}")
            
            # Example 4: Create a new page (commented out to avoid creating pages accidentally)
            """
            print("\n=== Creating a new page ===")
            try:
                result = await session.call_tool(
                    "create_page", 
                    arguments={
                        "title": "Test Page from MCP Client", 
                        "spaceKey": "COD",
                        "content": "<p>This is a test page created by the MCP client.</p>"
                    }
                )
                await print_json(result)
                
                # If we created a page, delete it to clean up
                if "id" in result:
                    page_id = result["id"]
                    print(f"\n=== Deleting page {page_id} ===")
                    delete_result = await session.call_tool(
                        "delete_page", 
                        arguments={"pageId": page_id}
                    )
                    await print_json(delete_result)
            except Exception as e:
                print(f"Error creating/deleting page: {str(e)}")
            """

if __name__ == "__main__":
    asyncio.run(run_examples())
