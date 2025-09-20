from crewai_tools import tool
from ..utils import mcp_tool

@tool("Get Pull Requests")
def get_pull_requests(owner: str, repo: str) -> str:
    """Fetch and provide a list of 5 most recently created pull requests from a GitHub repository."""
    result = mcp_tool(['tools', 'list_pull_requests', '--owner', owner, '--repo', repo, '--limit', '5'])
    return result