import unittest

from heap_sort import heap_sort
from .sort_testing_mixin import TestSortMixin


class HeapSortTestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = heap_sort


if __name__ == '__main__':
    unittest.main()
