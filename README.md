# Confluence MCP Server

A Model Context Protocol (MCP) server for interacting with Confluence Data Center via REST API. This server provides a set of tools that allow AI models to interact with Confluence content.

## Features

This MCP server provides the following operations for Confluence:

- Execute CQL (Confluence Query Language) searches
- Get page content by ID
- Get page content with body
- Find pages by space key
- Find page by title and space key
- Create new pages (with optional parent page)
- Update existing pages
- Delete pages

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with the following variables:

```
CONFLUENCE_API_BASE=http://localhost:8090/rest/api
CONFLUENCE_USERNAME=your_username
CONFLUENCE_PASSWORD=your_password
```

Adjust the values to match your Confluence instance.

## Running the Server

### Development Mode (Recommended)

The proper way to run an MCP server is using the MCP CLI tool with the development mode. This will start the MCP Inspector UI which allows you to test and debug the server:

```bash
mcp dev confluence.py
```

This will start the MCP Inspector at http://127.0.0.1:6274 by default.

### Direct Execution (Not Recommended)

MCP servers are designed to be run with the MCP CLI tool or integrated with Claude Desktop. Direct execution with Python is not the standard way to run an MCP server, but the script includes a fallback mode for testing:

```bash
python confluence.py
```

However, this mode has limited functionality and is only intended for basic testing.

### Installing in Claude Desktop

To install the server in Claude Desktop:

```bash
mcp install confluence.py
```

## API Reference

### execute_cql_search

Execute a CQL query on Confluence to search pages.

**Parameters:**
- `cql`: CQL query string
- `limit`: Number of results to return (default: 10)

### get_page_content

Get the content of a Confluence page.

**Parameters:**
- `pageId`: Confluence Page ID

### get_page_with_body

Get a page with its body content.

**Parameters:**
- `pageId`: Confluence Page ID

### find_pages_by_space

Find pages by space key.

**Parameters:**
- `spaceKey`: Confluence Space Key
- `limit`: Maximum number of results to return (default: 10)
- `expand`: Optional comma-separated list of properties to expand

### find_page_by_title

Find a page by title and space key.

**Parameters:**
- `title`: Page title
- `spaceKey`: Confluence Space Key

### create_page

Create a new page in Confluence.

**Parameters:**
- `title`: Page title
- `spaceKey`: Confluence Space Key
- `content`: Page content in storage format (HTML)
- `parentId`: Optional parent page ID

### update_page

Update an existing page in Confluence.

**Parameters:**
- `pageId`: Confluence Page ID
- `content`: New page content in storage format (HTML)
- `title`: Optional new title for the page
- `spaceKey`: Optional space key (only needed if changing space)

### delete_page

Delete a page by ID.

**Parameters:**
- `pageId`: Confluence Page ID

## Example Usage

Once the server is running and connected to an AI model, you can interact with Confluence using natural language. For example:

- "Find all pages in the DOCS space"
- "Get the content of page with ID 123456"
- "Create a new page titled 'Meeting Notes' in the TEAM space with content '<p>Notes from our meeting</p>'"
- "Update page with ID 123456 to have the content '<p>Updated meeting notes</p>'"
- "Update the title of page 123456 to 'Revised Meeting Notes'"

## License

MIT
