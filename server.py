from typing import Any, Dict, List, Optional, Union
import os
import base64
import json
import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass
from collections.abc import AsyncIterator

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import Context, FastMCP

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
CONFLUENCE_API_BASE = os.environ.get("CONFLUENCE_API_BASE", "http://localhost:8090/rest/api")
CONFLUENCE_USERNAME = os.environ.get("CONFLUENCE_USERNAME", "admin")
CONFLUENCE_PASSWORD = os.environ.get("CONFLUENCE_PASSWORD", "admin")

# Initialize FastMCP server
mcp = FastMCP("confluence")

@dataclass
class ConfluenceContext:
    """Context for Confluence API client."""
    client: httpx.AsyncClient

@asynccontextmanager
async def confluence_lifespan(server: FastMCP) -> AsyncIterator[ConfluenceContext]:
    """Manage Confluence API client lifecycle."""
    # Create auth header
    auth_str = f"{CONFLUENCE_USERNAME}:{CONFLUENCE_PASSWORD}"
    auth_bytes = auth_str.encode('ascii')
    auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
    
    # Initialize HTTP client with authentication
    async with httpx.AsyncClient(
        base_url=CONFLUENCE_API_BASE,
        headers={
            "Authorization": f"Basic {auth_b64}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        timeout=30.0
    ) as client:
        logger.info(f"Initialized Confluence API client for {CONFLUENCE_API_BASE}")
        yield ConfluenceContext(client=client)

# Set up lifespan context
mcp = FastMCP("confluence", lifespan=confluence_lifespan)

# Helper functions
async def handle_response(response: httpx.Response) -> Dict[str, Any]:
    """Handle API response, raising appropriate exceptions for errors."""
    try:
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error: {e.response.status_code}"
        try:
            error_data = e.response.json()
            error_msg = f"{error_msg} - {error_data.get('message', 'Unknown error')}"
        except Exception:
            error_msg = f"{error_msg} - {e.response.text or 'No error details'}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except Exception as e:
        logger.error(f"Error processing response: {str(e)}")
        raise ValueError(f"Failed to process response: {str(e)}")

# MCP Tools for Confluence API
@mcp.tool()
async def execute_cql_search(ctx: Context, cql: str, limit: int = 10) -> Dict[str, Any]:
    """
    Execute a CQL query on Confluence to search pages.
    
    Args:
        cql: CQL query string
        limit: Number of results to return
        
    Returns:
        Search results
    """
    client = ctx.request_context.lifespan_context.client
    params = {"cql": cql, "limit": limit}
    
    logger.info(f"Executing CQL search: {cql} with limit {limit}")
    response = await client.get("/content/search", params=params)
    return await handle_response(response)

@mcp.tool()
async def get_page_content(ctx: Context, pageId: str) -> Dict[str, Any]:
    """
    Get the content of a Confluence page.
    
    Args:
        pageId: Confluence Page ID
        
    Returns:
        Page content
    """
    client = ctx.request_context.lifespan_context.client
    
    logger.info(f"Getting page content for page ID: {pageId}")
    response = await client.get(f"/content/{pageId}")
    return await handle_response(response)

@mcp.tool()
async def get_page_with_body(ctx: Context, pageId: str) -> Dict[str, Any]:
    """
    Get a page with its body content.
    
    Args:
        pageId: Confluence Page ID
        
    Returns:
        Page with body content
    """
    client = ctx.request_context.lifespan_context.client
    
    logger.info(f"Getting page with body for page ID: {pageId}")
    response = await client.get(f"/content/{pageId}?expand=body.storage")
    return await handle_response(response)

@mcp.tool()
async def find_pages_by_space(ctx: Context, spaceKey: str, limit: int = 10, expand: Optional[str] = None) -> Dict[str, Any]:
    """
    Find pages by space key.
    
    Args:
        spaceKey: Confluence Space Key
        limit: Maximum number of results to return
        expand: Optional comma-separated list of properties to expand
        
    Returns:
        List of pages in the space
    """
    client = ctx.request_context.lifespan_context.client
    
    params = {"spaceKey": spaceKey, "limit": limit}
    if expand:
        params["expand"] = expand
    
    logger.info(f"Finding pages in space: {spaceKey}")
    # Use scan endpoint for better performance in Confluence 7.18+
    try:
        response = await client.get("/content/scan", params=params)
        return await handle_response(response)
    except Exception as e:
        logger.warning(f"Scan endpoint failed, falling back to standard endpoint: {str(e)}")
        response = await client.get("/content", params=params)
        return await handle_response(response)

@mcp.tool()
async def find_page_by_title(ctx: Context, title: str, spaceKey: str) -> Dict[str, Any]:
    """
    Find a page by title and space key.
    
    Args:
        title: Page title
        spaceKey: Confluence Space Key
        
    Returns:
        Page details if found
    """
    client = ctx.request_context.lifespan_context.client
    
    params = {"title": title, "spaceKey": spaceKey}
    
    logger.info(f"Finding page by title: {title} in space: {spaceKey}")
    response = await client.get("/content", params=params)
    return await handle_response(response)

@mcp.tool()
async def create_page(
    ctx: Context, 
    title: str, 
    spaceKey: str, 
    content: str, 
    parentId: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new page in Confluence.
    
    Args:
        title: Page title
        spaceKey: Confluence Space Key
        content: Page content in storage format (HTML)
        parentId: Optional parent page ID
        
    Returns:
        Created page details
    """
    client = ctx.request_context.lifespan_context.client
    
    # Prepare page data
    page_data = {
        "type": "page",
        "title": title,
        "space": {"key": spaceKey},
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }
    
    # Add parent if specified
    if parentId:
        page_data["ancestors"] = [{"id": parentId}]
    
    logger.info(f"Creating page: {title} in space: {spaceKey}")
    response = await client.post("/content", json=page_data)
    return await handle_response(response)

@mcp.tool()
async def delete_page(ctx: Context, pageId: str) -> Dict[str, Any]:
    """
    Delete a page by ID.
    
    Args:
        pageId: Confluence Page ID
        
    Returns:
        Deletion status
    """
    client = ctx.request_context.lifespan_context.client
    
    logger.info(f"Deleting page with ID: {pageId}")
    response = await client.delete(f"/content/{pageId}")
    
    if response.status_code == 204:
        return {"status": "success", "message": f"Page {pageId} deleted successfully"}
    
    return await handle_response(response)

# This server is designed to be run with the MCP CLI tool
# To run it, use: mcp dev server.py

# If you want to run it directly (not recommended), you can use this code
if __name__ == "__main__":
    print("=== Confluence MCP Server ===")
    print("This server is designed to be run with the MCP CLI tool.")
    print("To run it properly, use: mcp dev server.py")
    print("\nAttempting to start in direct mode (for testing only)...")
    
    try:
        import asyncio
        from mcp.server.stdio import stdio_server
        
        async def run():
            # This is a simplified version that works for direct execution
            async with stdio_server() as (read, write):
                await mcp.start(read, write)
        
        # Run the server
        asyncio.run(run())
    except Exception as e:
        print(f"\nError starting server: {e}")
        print("\nPlease use 'mcp dev server.py' instead.")
