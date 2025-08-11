# github-repo-template

## Requirements:

After creating a repo from this template and cloning the new repo to your local machine, run this command in the project root directory:
```bash
git config core.hooksPath .githooks
```

## Features:

- There is a .gitignore file tailored to Python/HuggingFace projects.

- The project root directory contains a `.githooks/` directory inside which there is a pre-commit script intended to prevent committing any file larger than a certain size, for example, 10MB. If your commit is blocked by the pre-commit script:
  - Run `git reset [BIG_FILE_OR_DIRECTORY_NAME]`
  - Add the oversized file or directory to the `.gitignore` file.

- To enable a `~/.gitignore_global` file for JetBrains (PyCharm, etc.) projects(or other projects), create the global gitignore file and configure git as follows:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

