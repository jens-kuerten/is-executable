## is-executable (pre-commit hook)
This Pre-commit hook can be used to check if files are marked as executable (755).

The hook uses `git ls-files --stage` which means it will also work on windows, but will only work on staged files. Having this work on windows is useful, if you develop for Linux on a Windows machine.

Example usage
```yaml
- repo: https://github.com/jens-kuerten/is-executable
    rev: 0.1.0
    hooks:
        - id: is-executable
        name: Check if scripts are marked as executable.
        files: ^some-folder/.*\.(sh|py)$
```
