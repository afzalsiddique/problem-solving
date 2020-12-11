import unittest
from leetcode.lc63 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        obstacleGrid = [[0,1],[0,0]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        obstacleGrid = [[1]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        obstacleGrid = [[1,0]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        obstacleGrid = [[0,0],[1,1],[0,0]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        obstacleGrid = [[0,0]]
        actual = solution.uniquePathsWithObstacles(obstacleGrid)
        expected = 1
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
