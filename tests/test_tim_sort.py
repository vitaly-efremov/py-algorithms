import unittest

from tim_sort import tim_sort
from tests import CommonSortMixin


class BubbleSortTestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = tim_sort

if __name__ == '__main__':
    unittest.main()
