import unittest

from quick_sort import quick_sort_classic, quick_sort
from .sort_testing_mixin import TestSortMixin


class QuickSortClassicTestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort_classic


class QuickSortPythonicTestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort


class QuickSortShortTestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort


if __name__ == '__main__':
    unittest.main()
