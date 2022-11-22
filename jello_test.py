from jello import add
from unittest import TestCase

class RunTests(TestCase):
    def test_add(self):
        self.assertEqual(add(5,5), 10)

