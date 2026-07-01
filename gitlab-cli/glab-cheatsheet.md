# GitLab CLI Cheatsheet

GitLab CLI is called `glab`.

It allows you to work with GitLab from the terminal, similar to how `gh` works for GitHub.

## Why DevOps Engineers Use It

DevOps engineers use `glab` to:

- Check pipeline status
- Review merge requests
- Create issues
- Inspect repositories
- Retry failed CI/CD jobs
- Automate GitLab workflows from scripts


## Authentication

Before using GitLab CLI, you must authenticate to a GitLab instance.

```bash
glab auth login

## Pipelines (CI/CD)

List recent pipelines:

```bash
glab pipeline list
```

View details about a pipeline:

```bash
glab pipeline view <pipeline-id>
```

View live pipeline logs:

```bash
glab pipeline ci view
```

Retry a failed pipeline:

```bash
glab pipeline retry <pipeline-id>
```

Cancel a running pipeline:

```bash
glab pipeline cancel <pipeline-id>
```

### Why This Matters

DevOps engineers frequently use these commands to:

- Monitor CI/CD jobs
- Investigate failed builds
- Retry failed pipelines
- View logs without opening the web UI


## Pipeline Debugging Notes

A pipeline can be created but still fail if:

- The `.gitlab-ci.yml` file is invalid
- No jobs match the pipeline rules
- No GitLab Runner is available
- The project runner configuration needs setup

Useful debugging commands:

```bash
glab pipeline list
glab ci view
glab ci lint


## Merge Requests

A Merge Request (MR) in GitLab is equivalent to a Pull Request (PR) in GitHub.

Create a new Merge Request:

```bash
glab mr create
```

List all Merge Requests:

```bash
glab mr list
```

View a specific Merge Request:

```bash
glab mr view <mr-id>
```

Checkout a Merge Request locally:

```bash
glab mr checkout <mr-id>
```

Merge an approved Merge Request:

```bash
glab mr merge <mr-id>
```

### Typical Workflow

1. Create a feature branch.
2. Make code changes.
3. Commit changes.
4. Push the branch.
5. Create a Merge Request using `glab mr create`.
6. Review and merge changes.