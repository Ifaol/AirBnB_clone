#!/usr/bin/python3
"""Unit tests for the Airbnb Command Line Interface."""
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestAirbnbCLI(unittest.TestCase):
    """Test cases for the Airbnb Command Line Interface."""

    def setUp(self) -> None:
        """Set up test environment."""
        super().setUp()

    def tearDown(self) -> None:
        """Tear down test environment."""
        super().tearDown()

    def test_show_command_help(self):
        """Test if the help message for the 'show' command is displayed."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            help_output = f.getvalue().strip()
            self.assertIn("show <class> <id>", help_output)
            self.assertIn("Display the string representation", help_output)

