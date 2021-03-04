import unittest
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s<target:
                        l+=1
                    elif s>target:
                        r-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while nums[l] == nums[l+1] and l+1<r:
                            l+=1
                        while nums[r] == nums[r-1] and l<r-1:
                            r-=1
                        l+=1
                        r-=1
        return res


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0)
        expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.fourSum(nums = [], target = 0)
        expected = []
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.fourSum([-2,-1,-1,1,1,2,2], 0)
        expected = [[-2,-1,1,2],[-1,-1,1,1]]
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.fourSum([0,0,0,0], 0)
        expected = [[0,0,0,0]]
        self.assertEqual(expected, actual)

