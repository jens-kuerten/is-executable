from unittest import TestCase
from unittest.mock import patch
import sys
import os
from is_executable.main import main


class TestMain(TestCase):
    def test_main_executable(self):
        # test that an executable file is detected correctly
        testargs = ["script.py", "./tests/fixtures/executable.sh"]

        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(0, ret)

    def test_main_not_executable(self):
        # test that a nonnexecutable file is detected
        testargs = ["script.py", "./tests/fixtures/not-executable.sh"]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)

    def test_unstaged_file(self):
        # test that unstaged files return non-zero exit code
        filepath = "./tests/fixtures/not-staged.sh"
        with open(filepath, "w"):
            pass
        testargs = ["script.py", filepath]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)

        os.remove(filepath)

    def test_main_not_exists(self):
        # test that we return a non-zero code if a file doesn't exist
        testargs = ["script.py", "./tests/fixtures/not-exists"]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)

    def test_pass_multiple_files_executable(self):
        # test passing multiple executable files
        testargs = [
            "script.py",
            "./tests/fixtures/executable.sh",
            "./tests/fixtures/executable2.sh",
        ]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(0, ret)

    def test_pass_multiple_files_not_executable(self):
        # test passing multiple files works and a non-executable is detected
        testargs = [
            "script.py",
            "./tests/fixtures/executable.sh",
            "./tests/fixtures/not-executable.sh",
        ]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)
