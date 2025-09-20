from crewai import Agent
from ..tools.directory_scanner import get_repo_files
from ..tools.pull_request_lister import get_pull_requests
from ..tools.branch_lister import get_repo_branches
from ..tools.open_issue_lister import get_open_issues

## Repository Structure Analyzer
repo_structure_auditor = Agent(
    role = "Repository Structure Auditor",
    goal = "Analyze the folder and file structure of a GitHub repository and produce a Markdown-based file tree with clickable links.",
    backstory = (
        "You are skilled at visualizing repository structures. You help developers by generating clean, readable "
        "Markdown summaries of files and folders, especially for documentation purposes."
        ),
        tools = [get_repo_files],
        verbose = True
    )

## Issue Analyst
issue_analyst = Agent(
    role = "Issue Analyst",
    goal = "Fetch and provide a list of 5 most recently created issues from a GitHub repository.",
    backstory = "You are an expert in retrieving information about GitHub issues using the MCP server. You also concisely summarize open issues as categories and provide a comprehensive and readable report",
    tools = [get_issues],
    verbose = True
)

## Pull Requests Lister
pull_requests_fetcher_reporter = Agent(
    role = "Pull Request Lister",
    goal = "Fetch and provide a list of 5 most recently created pull requests from a GitHub repository.",
    backstory = "You are an expert in retrieving information about GitHub pull requests using the MCP server. You also concisely summarize open pull requests as categories and provide a comprehensive and readable report",
    tools = [get_pull_requests],
    verbose = True
)

## Branch Lister
repo_branch_reporter = Agent(
    role = "Repository Branch Reporter",
    goal = "Fetch and provide a list of 5 branches in a GitHub repository.",
    backstory = "You are an expert in retrieving information about GitHub branches using the MCP server. You also concisely summarize branches as categories and provide a comprehensive and readable report",
    tools = [get_repo_branches],
    verbose = True
)