import unittest
from Algorithm_Course.lab01.task2_1 import *

class MyTestCase(unittest.TestCase):
    def test_find_median1(self):
        arr = [1,3,4]
        expected = 3
        actual = find_median(arr, len(arr))
        self.assertEqual(expected, actual)


    def test_find_median2(self):
        arr = [1,3,4,60]
        expected = 3
        actual = find_median(arr, len(arr))
        self.assertEqual(expected, actual)


    def test_find_median3(self):
        arr = [1,3,4,60,70]
        expected = 4
        actual = find_median(arr, len(arr))
        self.assertEqual(expected, actual)


    def test_find_median4(self):
        arr = [1,3,4,60,70,50,2]
        expected = 4
        actual = find_median(arr, len(arr))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
