# https://www.youtube.com/watch?v=m18Hntz4go8
import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l_max, r_max = [0 for _ in range(n)], [0 for _ in range(n)] # prefix max and suffix max
        maxx = 0
        for i in range(n):
            maxx = max(maxx, height[i])
            l_max[i] = maxx
        maxx=0
        for i in reversed(range(n)):
            maxx = max(maxx, height[i])
            r_max[i] = maxx

        ans=0
        for i in range(n):
            minn = min(l_max[i],r_max[i])
            ans+= minn - height[i]
        return ans


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.trap([4,2,0,3,2,5])
        expected = 9
        self.assertEqual(expected, actual)

