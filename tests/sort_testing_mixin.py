class TestSortMixin(object):
    def setUp(self):
        raise NotImplementedError('Merge function is not specified.')

    def test_empty_array(self):
        sorted_list = self.sort_func([])
        self.assertListEqual(sorted_list, [])

    def test_one_element(self):
        sorted_list = self.sort_func([1])
        self.assertListEqual(sorted_list, [1])

    def test_two_elements(self):
        sorted_list = self.sort_func([1, 2])
        self.assertListEqual(sorted_list, [1, 2])

    def test_ordered_elements(self):
        sorted_list = self.sort_func([1, 2, 3, 4])
        self.assertListEqual(sorted_list, [1, 2, 3, 4])

    def test_unordered_elements_odd_count(self):
        sorted_list = self.sort_func([9, 6, 1, 2, 0, 4, 1])
        self.assertListEqual(sorted_list, [0, 1, 1, 2, 4, 6, 9])

    def test_unordered_elements_even_count(self):
        sorted_list = self.sort_func([2, 3, -1, 5, 0, 8, 9, 7])
        self.assertListEqual(sorted_list, [-1, 0, 2, 3, 5, 7, 8, 9])
