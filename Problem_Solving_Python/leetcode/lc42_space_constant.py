# https://www.youtube.com/watch?v=m18Hntz4go8
import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        ans=0
        l_max,r_max=0,0
        while l<=r:
            if l_max<=r_max:
                if l_max<=height[l]:
                    l_max=height[l]
                else:
                    ans+=l_max-height[l]
                l+=1
            else:
                if r_max<=height[r]:
                    r_max=height[r]
                else:
                    ans+=r_max-height[r]
                r-=1
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

    def test_3(self):
        sol = Solution()
        actual = sol.trap([])
        expected = 0
        self.assertEqual(expected, actual)
