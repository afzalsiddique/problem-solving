import unittest
from Algorithm_Course.lab01.task1_1 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [2,6,4,1,6,2]
        expected = sorted(arr)
        actual = merge_sort(arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        arr = [2, 1, 4, 3, 5, 9, 8]
        expected = sorted(arr)
        actual = merge_sort(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
