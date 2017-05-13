import unittest

from tim_sort import tim_sort
from .sort_testing_mixin import TestSortMixin


class BubbleSortTestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = tim_sort


if __name__ == '__main__':
    unittest.main()
