import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        maxx = -1
        while left != right:
            if height[left] < height[right]:
                limited_by_left = True
            else:
                limited_by_left = False
            area = min(height[left], height[right]) * (right - left)
            if area > maxx:
                maxx = area

            if limited_by_left:
                left += 1
            else:
                right -= 1
        return maxx

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.maxArea(height = [1,8,6,2,5,4,8,3,7])
        expected = 49
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.maxArea(height = [1,1])
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.maxArea(height = [4,3,2,1,4])
        expected = 16
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.maxArea(height = [1,2,1])
        expected = 2
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.maxArea([1,0,0,0,0,0,0,2,2])
        expected = 8
        self.assertEqual(expected, actual)

