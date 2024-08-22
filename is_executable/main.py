#!/usr/bin/env python3
"""
Checks if the given files are marked as executable.
You can pass multiple files, separated by a space.
"""

import subprocess  # nosec
import sys


def is_executable_with_git(filepath):
    """Check if a file is executable using Git."""
    try:
        # Run `git ls-files --stage <filepath>` to get the file mode
        result = subprocess.run(  # nosec
            ["git", "ls-files", "--stage", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        # The output looks like: "100755 <hash> 0 <filename>"
        # The first part (100755) is the file mode. 100755 indicates an executable file.
        if result.stdout.startswith("100755"):
            return True
    except subprocess.CalledProcessError:
        pass
    return False


def main():
    non_executable_files = []

    # Iterate over all files passed to the script
    for filepath in sys.argv[1:]:
        if not is_executable_with_git(filepath):
            non_executable_files.append(filepath)

    if non_executable_files:
        print("The following files are not marked as executable:")
        for filepath in non_executable_files:
            print(f"- {filepath}")

        print("You can fix this with: git update-index --chmod=+x <file>")
        return 1  # Non-zero exit code to indicate failure

    return 0  # Zero exit code to indicate success


if __name__ == "__main__":
    sys.exit(main())
