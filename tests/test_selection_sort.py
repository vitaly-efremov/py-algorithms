import unittest
from selection_sort import selection_sort_v1, selection_sort_v2
from .sort_testing_mixin import TestSortMixin


class SelectionSortV1TestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = selection_sort_v1


class SelectionSortV2TestCase(TestSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = selection_sort_v2


if __name__ == '__main__':
    unittest.main()
