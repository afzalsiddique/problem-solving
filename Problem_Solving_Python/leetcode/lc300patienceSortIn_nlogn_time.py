# https://www.youtube.com/watch?v=elqKCreFLAc
# https://www.youtube.com/watch?v=22s1xxRvy28
from typing import List


class Solution:
    def lengthOfLIS(self, nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub) - 1
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)


import unittest
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(4, solution.lengthOfLIS([10,9,2,5,3,7,101,18]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.lengthOfLIS([0,1,0,3,2,3]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(1, solution.lengthOfLIS([7,7,7,7,7,7,7]))

    def test_4(self):
        solution = Solution()
        self.assertEqual(6, solution.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

    def test_5(self):
        solution = Solution()
        self.assertEqual(3, solution.lengthOfLIS([1,6,7,3]))

    def test_6(self):
        solution = Solution()
        self.assertEqual(3, solution.lengthOfLIS([1,6,7]))

    def test_7(self):
        solution = Solution()
        self.assertEqual(6, solution.lengthOfLIS([2,5,3,4,11,8,10,13,6]))