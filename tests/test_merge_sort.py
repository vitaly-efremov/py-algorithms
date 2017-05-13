import unittest
from merge_sort import merge_sort_v1, merge_sort_v2
from tests import CommonSortMixin


class MergeSortV1TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = merge_sort_v1


class MergeSortV2TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = merge_sort_v2

if __name__ == '__main__':
    unittest.main()
