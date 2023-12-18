from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution2()

# https://www.youtube.com/watch?v=jzZsG8n2R9A
class Solution2:
    # two pointer
    # time:n^2 space:1
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0: break  # optimization. nums sorted, impossible for nums[i]+nums[l]+nums[r] == 0
            if i > 0 and nums[i] == nums[i - 1]: continue # prevent duplicates in result
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s==0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1 # skip duplicates
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l+=1
                    r-=1
                if s < 0:
                    l += 1
                elif s>0:
                    r -= 1
        return res


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time:n^2 space: n
        # based on two sum using sett
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

class Solution:
    # n^2*log n
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
    def test01(self):
        e=[[-1,0,1]]
        a=get_sol().threeSum([-1,0,1,-1,0,1])
        self.assertEqual([sorted(x) for x in e],[sorted(x) for x in a])
    def test02(self):
        a=get_sol().threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        e=[[0,0,0]]
        self.assertEqual([sorted(x) for x in e],[sorted(x) for x in a])
    def test03(self):
        a = get_sol().threeSum(nums = [-1,0,1,2,-1,-4])
        e = [[-1,-1,2],[-1,0,1]]
        self.assertEqual([sorted(x) for x in e],[sorted(x) for x in a])
    def test04(self):
        e=[[1,1,-2]]
        a=get_sol().threeSum([1,1,-2])
        self.assertEqual([sorted(x) for x in e],[sorted(x) for x in a])
