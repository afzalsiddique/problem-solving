import unittest
from leetcode.leetcode973 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        points = [[3,3],[5,-1],[-2,4]]
        K = 2
        actual = solution.kClosest(points, K)
        expected = [[3,3],[-2,4]]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        points = [[1,3],[-2,2]]
        K = 1
        actual = solution.kClosest(points, K)
        expected = [[-2,2]]
        self.assertEqual(expected, actual)


    def test_3(self):
        solution = Solution()
        points = [[3,3],[5,-1],[-2,4],[1,1]]
        K = 2
        actual = solution.kClosest(points, K)
        expected = [[1,1],[3,3]]
        self.assertEqual(expected, actual)






if __name__ == '__main__':
    unittest.main()
