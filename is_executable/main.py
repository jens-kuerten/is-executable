"""
Checks if the given files are marked as executable.
You can pass multiple files, separated by a space.
"""

import subprocess  # nosec
import sys
import os.path

def is_executable_with_git(filepath):
    """Check if a file is executable using Git."""

    # Run `git ls-files --stage <filepath>` to get the file mode
    result = subprocess.run(  # nosec
        ["git", "ls-files", "--stage", filepath],
        stdout=subprocess.PIPE,
        text=True,  # output should be treated as string rather than bytes
        check=True,  # non zero exit code should raise exception
    )

    # The output looks like: "100755 <hash> 0 <filename>"
    # The first part (100755) is the file mode. 100755 indicates an executable file.
    if result.stdout.startswith("100755"):
        return True

    if result.stdout == "":
        # git ls-files returns nothing if the file could not be found or if it is not staged
        print(f"{filepath} is not staged or does not exist")
    return False


def main():
    non_executable_files = []

    for filepath in sys.argv[1:]:
        if not os.path.isfile(filepath):
            print(f"{filepath} does not exist!")
            return 1  # Non-zero exit code to indicate failure
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
