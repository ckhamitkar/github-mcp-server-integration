from crewai_tools import tool
from ..utils import mcp_tool

@tool("Get Repo Branches")
def get_repo_branches(owner: str, repo: str) -> str:
    """Fetch and provide a list of 5 branches of the GitHub repository using the MCP server."""
    result = mcp_tool(['tools', 'list_branches', '--owner', owner, '--repo', repo, '--limit', '5'])
    return result