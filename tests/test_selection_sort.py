import unittest
from selection_sort import selection_sort_v1, selection_sort_v2
from tests import CommonSortMixin


class SelectionSortV1TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = selection_sort_v1


class SelectionSortV2TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = selection_sort_v2

if __name__ == '__main__':
    unittest.main()
