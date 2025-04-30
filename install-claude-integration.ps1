# PowerShell script to install the Confluence MCP server in Claude Desktop
# Run this script from the project directory

# Check if MCP is installed
try {
    $mcpVersion = (uv run mcp --version) 2>&1
    Write-Host "Found MCP: $mcpVersion"
} catch {
    Write-Host "MCP CLI not found. Installing required packages..."
    uv pip install "mcp[cli]"
}

# Ensure we're in the right directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Check if config file exists
$configFile = "confluence-mcp-config.json"
if (-not (Test-Path $configFile)) {
    Write-Host "Configuration file not found: $configFile"
    exit 1
}

# Install the MCP server in Claude Desktop
Write-Host "Installing Confluence MCP server in Claude Desktop..."
uv run mcp install --config $configFile

Write-Host "`nInstallation complete!"
Write-Host "To verify the installation, open Claude Desktop and check the MCP Servers section in Settings."
Write-Host "You can now use Claude to interact with your Confluence instance."
