import unittest
from Algorithm_Course.lab01.task1_1 import *


class MyTestCase(unittest.TestCase):
    def test_final1(self):
        arr = [3, 1, 5]
        k = 2
        expected = (1, 3)
        actual = final(arr, k)
        self.assertEqual(expected, actual)

    def test_final2(self):
        arr = [1, 1, 3, 3]
        k = 11
        expected = (3, 1)
        actual = final(arr, k)
        self.assertEqual(expected, actual)

    def test_merge_sort1(self):
        arr = [(3, 3), (3, 1), (3, 5), (1, 3), (1, 1), (1, 5), (5, 3), (5, 1), (5, 5)]
        expected = sorted(arr)
        actual = merge_sort(arr)
        self.assertEqual(expected, actual)

    def test_merge_sort2(self):
        arr = [(1, 1), (1, 1), (1, 3), (1, 3), (1, 1), (1, 1), (1, 3), (1, 3), (3, 1), (3, 1), (3, 3), (3, 3), (3, 1),
               (3, 1), (3, 3), (3, 3)]
        expected = sorted(arr)
        actual = merge_sort(arr)
        self.assertEqual(expected, actual)

    def test_is_less_than_or_equal1(self):
        a = (1, 3)
        b = (2, 3)
        expected = True
        actual = is_less_than_or_equal(a, b)
        self.assertEqual(expected, actual)

    def test_is_less_than_or_equal2(self):
        a = (1, 3)
        b = (1, 3)
        expected = True
        actual = is_less_than_or_equal(a, b)
        self.assertEqual(expected, actual)

    def test_is_less_than_or_equal3(self):
        a = (1, 2)
        b = (1, 3)
        expected = True
        actual = is_less_than_or_equal(a, b)
        self.assertEqual(expected, actual)

    def test_is_less_than_or_equal4(self):
        a = (2, 2)
        b = (1, 3)
        expected = False
        actual = is_less_than_or_equal(a, b)
        self.assertEqual(expected, actual)

    def test_is_less_than_or_equal5(self):
        a = (1, 3)
        b = (1, 1)
        expected = False
        actual = is_less_than_or_equal(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
