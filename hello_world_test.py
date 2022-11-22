from hello_world import hello
from unittest import TestCase

class RunTests(TestCase):
    def test_add(self):
        self.assertEqual(hello(), "Hello World!!")
