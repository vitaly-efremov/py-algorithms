import unittest

from quick_sort import quick_sort_classic, quick_sort
from tests import CommonSortMixin


class QuickSortClassicTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort_classic


class QuickSortPythonicTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort


class QuickSortShortTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = quick_sort


if __name__ == '__main__':
    unittest.main()
