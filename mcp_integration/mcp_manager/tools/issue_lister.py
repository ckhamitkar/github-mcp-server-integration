from crewai_tools import tool
from ..utils import mcp_tool

@tool("Get Issues")
def get_issues(owner: str, repo: str) -> str:
    """Fetch and provide a list of 5 most recently created issues from a GitHub repository."""
    result = mcp_tool(['tools', 'list_issues', '--owner', owner, '--repo', repo, '--limit', '5'])
    return result