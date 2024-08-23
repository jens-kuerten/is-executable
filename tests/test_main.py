from unittest import TestCase
from unittest.mock import patch
import sys
from is_executable.main import main


class TestMain(TestCase):
    def test_main_executable(self):
        testargs = ["script.py", "./tests/fixtures/executable.sh"]

        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(0, ret)

    def test_main_not_executable(self):
        testargs = ["script.py", "./tests/fixtures/not-executable.sh"]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)

    def test_main_not_exists(self):
        testargs = ["script.py", "./tests/fixtures/not-exists"]
        with patch.object(sys, "argv", testargs):
            ret = main()
            self.assertEqual(1, ret)
