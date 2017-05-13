import unittest

from heap_sort import heap_sort
from tests import CommonSortMixin


class HeapSortTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = heap_sort

if __name__ == '__main__':
    unittest.main()
