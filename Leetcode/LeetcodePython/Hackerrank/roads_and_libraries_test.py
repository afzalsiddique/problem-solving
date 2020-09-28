import unittest

from Hackerrank.roads_and_libraries import *
class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 3
        c_road = 2
        c_lib = 1
        cities = [[1, 2], [3, 1], [2, 3]]
        solution = Solution()
        actual = solution.roadsAndLibraries(n, c_road, c_lib, cities)
        expected = 4
        self.assertEqual(expected, actual)
    def test_2(self):
        n = 6
        c_road = 2
        c_lib = 5
        cities = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
        solution = Solution()
        actual = solution.roadsAndLibraries(n, c_road, c_lib, cities)
        expected = 12
        self.assertEqual(expected, actual)
