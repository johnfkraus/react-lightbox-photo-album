# github-repo-template

## Requirements:

After creating a repo from this template and cloning the new repo to your local machine, run this command in the project root directory:
```bash
git config core.hooksPath .githooks
```

## Features:

### .gitignore

- The project has a .gitignore file tailored to Python/HuggingFace projects.

- To enable a `~/.gitignore_global` file for JetBrains (PyCharm, etc.) projects(or other projects), create the global gitignore file and configure git as follows:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

### Precommit script prevents commits containing oversized files

- The Github repository template's project root directory contains a `.githooks/` directory inside which there is a pre-commit script intended to prevent committing any file larger than a certain size.  GitHub recommends a maximum individual file size of 1MB, with a hard limit enforced at 100MB. Files exceeding 100MB will generally be blocked and require the use of Git Large File Storage (Git LFS) (at additional cost).  (Removing large files from a commit can be tedious.)
- The pre-commit script has a default maximum size of 10MB which you can change.  (This is to prevent Github from choking on and blocking large files.)  If your commit is blocked by the pre-commit script:
  - Run `git reset [BIG_FILE_OR_DIRECTORY_NAME]`
  - Add the oversized file or directory to the `.gitignore` file.

