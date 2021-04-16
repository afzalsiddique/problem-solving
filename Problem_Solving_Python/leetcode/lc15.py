# https://www.youtube.com/watch?v=jzZsG8n2R9A
import unittest
from bisect import bisect_left
from typing import List

# two pointer
# time:n^2 space:1
class Solution2:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # optimization
            if nums[i] > 0:
                break  # nums sorted, impossible for nums[i]+nums[l]+nums[r] == 0
            if i > 0 and nums[i] == nums[i - 1]: continue # prevent duplicates in result
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]: l += 1 # skip duplicates
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
        return res


# time:n^2 space: n
# based on two sum using sett
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =set()
        nums.sort()
        for i,a in enumerate(nums[:-2]):
            if i>0 and nums[i]==nums[i-1]:continue
            sett=set()
            for b in nums[i+1:]:
                if b in sett:
                    res.add((a,b,0-a-b))
                else:
                    sett.add(0-a-b)
        return list(map(list,res))

# n^2*log n
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res,n=[],len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:continue
                target = -(nums[i]+nums[j])
                idx = bisect_left(nums,target,j+1)
                if idx!=n and nums[idx]==target:
                    res.append([nums[i],nums[j],target])
        return res
## TLE
class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        def two_sum(temp_nums, target):
            sett=set()
            for num in temp_nums:
                if num in sett:
                    temp=sorted((num,target-num,0-target))
                    if temp in res:continue
                    res.append(temp)
                else:
                    sett.add(target-num)

        for i in range(len(nums)-1):
            temp_nums=nums[:i]+nums[i+1:]
            two_sum(temp_nums,0-nums[i])
        return list(map(list,res))

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.threeSum(nums = [-1,0,1,2,-1,-4])
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(expected, actual)

    def test1(self):
        self.assertEqual([[-1,0,1]],Solution().threeSum([-1,0,1,-1,0,1]))
    def test2(self):
        self.assertEqual([[0,0,0]],Solution().threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
