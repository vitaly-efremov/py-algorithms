import unittest
from heap import Heap


class HeapTestCase(unittest.TestCase):
    def setUp(self):
        self.array = [5, 3, 0, 1, 2]
        self.heap = Heap()

    def test_insert(self):
        for x in [5, 3, 0, 1, 2]:
            self.heap.insert(x)

        self.assertEqual(self.heap.array, [5, 3, 0, 1, 2])


if __name__ == '__main__':
    unittest.main()
