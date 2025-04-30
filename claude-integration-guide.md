# Integrating Confluence MCP Server with Claude Desktop

This guide explains how to integrate your Confluence MCP server with Claude Desktop, allowing Claude to interact with your Confluence instance through the MCP protocol.

## Prerequisites

- Claude Desktop installed
- Python 3.9+ installed
- `uv` and `mcp` packages installed
- Confluence server accessible

## Integration Methods

There are two ways to integrate your MCP server with Claude Desktop:

1. **Simple Installation** - Quick but with limited configuration
2. **JSON Configuration Installation** - More control and customization

## Method 1: Simple Installation

For a quick installation with default settings:

```bash
# Navigate to your project directory
cd path/to/mcp-confluence-server

# Install the server in Claude Desktop
mcp install server.py
```

## Method 2: JSON Configuration Installation (Recommended)

This method gives you more control over how your server is configured in Claude Desktop.

### Step 1: Edit the Configuration File

The `confluence-mcp-config.json` file contains all the settings for your MCP server. Customize it as needed:

- Update the `CONFLUENCE_API_BASE` to point to your Confluence instance
- Set the correct `CONFLUENCE_USERNAME` and `CONFLUENCE_PASSWORD`
- Modify the `metadata` section with your information

### Step 2: Install Using the Configuration File

```bash
# Navigate to your project directory
cd path/to/mcp-confluence-server

# Install with the configuration file
mcp install --config confluence-mcp-config.json
```

### Step 3: Verify Installation

1. Open Claude Desktop
2. Click on the "..." menu in the top-right corner
3. Select "Settings"
4. Go to the "MCP Servers" tab
5. Confirm that "Confluence Data Center" appears in the list of installed servers

## Using Custom Commands

If you need to customize how the server is run, you can modify the `command` and `args` fields in the configuration file:

```json
{
  "command": "python",
  "args": ["-m", "mcp", "run", "server.py"]
}
```

Or for using a virtual environment:

```json
{
  "command": ".venv/Scripts/python",
  "args": ["-m", "mcp", "run", "server.py"]
}
```

## Troubleshooting

If you encounter issues with the integration:

1. **Check Logs**: Claude Desktop logs can help identify issues
   ```bash
   mcp logs
   ```

2. **Test the Server**: Make sure the server runs correctly in development mode
   ```bash
   mcp dev server.py
   ```

3. **Reinstall**: If needed, uninstall and reinstall the server
   ```bash
   mcp uninstall confluence-server
   mcp install --config confluence-mcp-config.json
   ```

## Advanced Configuration Options

The JSON configuration supports additional options:

- `icon`: URL or path to an icon for the server in Claude Desktop
- `capabilities`: Specify which MCP capabilities your server supports
- `metadata`: Additional information about your server
- `env`: Environment variables for the server process

## Example: Complete Installation Command

Here's a complete example command that installs the server with all options:

```bash
mcp install --config confluence-mcp-config.json --name "Confluence Server" --description "Access Confluence content from Claude" --icon https://path/to/icon.png
```

However, when using a config file, the command-line options are usually not necessary as they're defined in the JSON file.
