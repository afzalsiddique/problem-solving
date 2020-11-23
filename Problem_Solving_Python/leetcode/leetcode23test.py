import unittest
from leetcode.leetcode23 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        lists = [
            [1,4,5],
            [2,6,8]
        ]
        actual = solution.mergeKLists(lists)
        expected = [1,2,4,5,6,8]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        lists = [
            [1,4,5],
            [2,6,8],
            [8,10]
        ]
        actual = solution.mergeKLists(lists)
        expected = [1,2,4,5,6,8,8,10]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        actual = solution.mergeKLists(lists)
        expected = [1,1,2,3,4,4,5,6]
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        lists = [[1, 4, 5], [2,6,8], [1,4,9],[8,10,11],[9,81]]
        actual = solution.mergeKLists(lists)
        expected = [1,1,2,4,4,5,6,8,8,9,9,10,11,81]
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
