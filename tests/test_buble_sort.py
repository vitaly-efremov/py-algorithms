import unittest

from bubble_sort import bubble_sort
from tests import CommonSortMixin


class BubbleSortTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = bubble_sort

if __name__ == '__main__':
    unittest.main()
