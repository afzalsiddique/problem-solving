import unittest
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        di, n = {}, len(nums)

        def dfs(target):
            if target==0:return 1
            if target<0: return 0
            if target in di:return di[target]
            ans = 0
            for i in range(n):
                ans += dfs(target-nums[i])
            di[target] = ans
            return ans

        return dfs(target)



class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        nums = [1,2,3]
        target = 4
        actual = solution.combinationSum4(nums, target)
        expected = 7
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [4,2,1]
        target = 32
        actual = solution.combinationSum4(nums, target)
        expected = 39882198
        self.assertEqual(expected, actual)

