import unittest
from insertion_sort import insertion_sort_v1, insertion_sort_v2
from tests import CommonSortMixin


class InsertSortV1TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = insertion_sort_v1


class InsertSortV2TestCase(CommonSortMixin, unittest.TestCase):
    def setUp(self):
        self.sort_func = insertion_sort_v2

if __name__ == '__main__':
    unittest.main()
