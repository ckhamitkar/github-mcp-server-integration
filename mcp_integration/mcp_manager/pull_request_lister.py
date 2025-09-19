def build_crew(owner: str, repo: str) -> Crew:
    tasks = []
    tasks.extend (analyze_repo_structure_task(owner,repo))
    tasks.extend (get_issue_tasks(owner, repo))

    return Crew(
        agents = [repo_structure_auditor, issue_analyst],
        tasks = tasks, 
        process = Process.sequential,
        verbose = True,
        cache = True,
    )