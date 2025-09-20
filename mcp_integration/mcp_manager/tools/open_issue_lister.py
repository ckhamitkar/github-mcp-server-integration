from crewai_tools import tool
from ..utils import mcp_tool

@tool("Get Open Issues")
def get_open_issues(owner: str, repo: str) -> str:
    """Fetch and provide a list of open issues from a GitHub repository using the MCP server."""
    result = mcp_tool(['tools', 'list_issues', '--owner', owner, '--repo', repo, '--state', 'open', '--limit', '5'])
    return result