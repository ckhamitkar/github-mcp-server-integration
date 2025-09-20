from crewai_tools import tool
from ..utils import mcp_tool

@tool("Get Repo Files")
def get_repo_files(owner: str, repo: str, path: str = ".") -> str:
    """List files and folders at a given path in a GitHub repository."""
    result = mcp_tool(['tools', 'get_file_contents', '--owner', owner, '--repo', repo, '--path', path])
    return result