# Tests for the command.py
from app import commands
import unittest


class TestCommands(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello(self):
        self.assertEqual(commands.hello(), "Hello, World!")

    def test_echo(self):
        teststring = "This should be echoed"
        self.assertEqual(commands.echo(teststring), teststring)

    def test_ping(self):
        self.assertEqual(commands.ping(), "pong!")

if __name__ == '__main__':
    unittest.main()
