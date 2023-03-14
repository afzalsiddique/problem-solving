from collections import Counter;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[Counter() for x in nums]
        res=0
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=dp[j][diff]+1
            res+=sum(dp[i].values())
        return res-(n*(n-1)//2)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,Solution().numberOfArithmeticSlices(nums = [2,4,6,8]))
    def test2(self):
        self.assertEqual(5,Solution().numberOfArithmeticSlices(nums = [7,7,7,7]))
    def test3(self):
        self.assertEqual(7,Solution().numberOfArithmeticSlices(nums = [2,4,6,8,10]))
    def test4(self):
        self.assertEqual(16,Solution().numberOfArithmeticSlices(nums = [7,7,7,7,7]))
    def test5(self):
        self.assertEqual(0,Solution().numberOfArithmeticSlices(nums = [0,2000000000,-294967296]))
