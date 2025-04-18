import unittest
from is_unique import is_unique

class TestIsUnique(unittest.TestCase):

    def test_unique_lists(self):
        self.assertTrue(is_unique([1, 2, 3]))
        self.assertTrue(is_unique(['a', 'b', 'c']))
        self.assertTrue(is_unique([]))

    def test_non_unique_lists(self):
        self.assertFalse(is_unique([1, 1, 2]))
        self.assertFalse(is_unique(['x', 'y', 'x']))
        self.assertFalse(is_unique([5, 5, 5, 5]))
