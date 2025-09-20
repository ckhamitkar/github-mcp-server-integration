# GEMINI.md - Directory Analysis: mcp_manager/templates/mcp_manager

## Directory Overview

This directory contains HTML templates for the `mcp_manager` Django application. These templates define the user interface for interacting with the GitHub MCP Server integration, primarily for generating and displaying documentation for GitHub repositories.

## Key Files

*   **`documentation_interface.html`**: This template provides a web form where users can input a GitHub repository URL to initiate the documentation generation process. It includes basic styling and an input field for the repository URL.
*   **`documentation_display.html`**: This template is responsible for displaying the generated documentation. It conditionally renders the documentation content (which is expected to be in Markdown format, converted to HTML) or a message indicating that no documentation has been generated yet. It also provides a link to return to the documentation generation interface.
*   **`mcp_interface.html`**: This template offers a direct interface for interacting with the GitHub MCP Server. It includes a form with fields for various MCP commands (e.g., `get_issue`, `list_issues`), repository owner, repository name, and issue number. This template appears to be intended for debugging or manual testing of the MCP server's functionalities.

## Usage

These templates are used by the Django `mcp_manager` application to render web pages for users.

*   `documentation_interface.html` is the entry point for users to request documentation.
*   `documentation_display.html` is used to present the results of the documentation generation.
*   `mcp_interface.html` provides a utility for developers or advanced users to directly test and interact with the underlying GitHub MCP Server commands.
