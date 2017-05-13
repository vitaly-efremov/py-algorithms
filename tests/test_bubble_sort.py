import unittest

from bubble_sort import bubble_sort
from .sort_testing_mixin import TestSortMixin


class TestBubbleSort(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = bubble_sort


if __name__ == '__main__':
    unittest.main()
