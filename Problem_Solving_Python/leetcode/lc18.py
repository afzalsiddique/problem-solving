from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def two_sum(self, l, r, target):
        A=self.A
        if l>r: return []
        res=[]
        while l<r:
            if A[l]+A[r]==target:
                res.append([A[l],A[r]])
                while l<r and A[l]==A[l+1]: l+=1
                while l<r and A[r]==A[r-1]: r-=1
            if A[l]+A[r]<target:
                l+=1
            else:
                r-=1
        return res
    def kSum(self,l,r,k,target):
        A=self.A
        if l>r: return []
        if k==2:
            return self.two_sum(l, r, target)
        res=[]
        for i in range(l,r):
            if i>l and A[i]==A[i-1]: continue
            ans=self.kSum(i+1,r,k-1,target-A[i])
            for sub in ans:
                tmp=[A[i]]+sub
                res.append(tmp)
        return res
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        self.A=A
        return self.kSum(0,len(A)-1,4,target)
class Solution3:
    def k_sum(self, nums, target, k): # kSum requires nums to be sorted
        if k == 2: return self.two_sum(nums, target)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]: continue
            res = self.k_sum(nums[i + 1:], target - nums[i], k - 1)
            for subresult in res:
                ans.append([nums[i]] + subresult)
        return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, 4)

    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        # version 1. hashset
        s, res = set(), []
        for i in range(len(nums)):
            # if i>0 and nums[i]==nums[i-1]:continue # Wrong -> [2,2]

            # If current value is already in the result list then avoid duplicates
            if len(res) != 0 and res[-1][0] == nums[i]: continue
            if target - nums[i] in s:
                res.append([nums[i], target - nums[i]])
            s.add(nums[i])
        return res

        # version 2. two pointers
        res = []
        l, r = 0, len(nums) - 1
        while l < r:
            temp = nums[l] + nums[r]
            if temp < target or (l > 0 and nums[l] == nums[l - 1]):
                l += 1
            elif temp > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res
        # version 3. hashMap
        di, res = {},[]
        for num in nums:
            if target-num in di and di[target-num]==True:
                res.append([target-num,num])
                di[target-num] = False
            else:
                if num not in di:
                    di[num] = True
        return res

class Solution2:
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
    # def test_two_sum1(self):
    #     actual = get_sol().two_sum([0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 5, 5, 6, 6, 6, 6, 8, 8, 8], 8)
    #     expected = [[3, 5], [2, 6], [0, 8]]
    #     self.assertEqual(sorted([sorted(x) for x in expected]), sorted([sorted(x) for x in actual])) # just sorted
    # def test_two_sum2(self):
    #     actual = get_sol().two_sum([0, 0, 0, 0], 0)
    #     expected = [[0, 0]]
    #     self.assertEqual(expected, actual)
    # def test_two_sum3(self):
    #     actual = get_sol().two_sum([2, 2], 4)
    #     expected = [[2, 2]]
    #     self.assertEqual(expected, actual)
    def test_1(self):
        actual = get_sol().fourSum([1, 0, -1, 0, -2, 2],0)
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted([sorted(x) for x in expected]), sorted([sorted(x) for x in actual])) # just sorted
    def test_2(self):
        actual = get_sol().fourSum([], 0)
        expected = []
        self.assertEqual(expected, actual)
    def test_3(self):
        actual = get_sol().fourSum([-2, -1, -1, 1, 1, 2, 2], 0)
        expected = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
        self.assertEqual(sorted([sorted(x) for x in expected]), sorted([sorted(x) for x in actual])) # just sorted
    def test_4(self):
        actual = get_sol().fourSum([0, 0, 0, 0], 0)
        expected = [[0, 0, 0, 0]]
        self.assertEqual(expected, actual)
    # def test_5(self):
    #     nums = sorted([-1,0,1,2,-1,-4])
    #     target = 0
    #     actual = get_sol().k_sum(nums, target,3)
    #     expected = [[-1, 1, 0], [-1, 2, -1]]
    #     self.assertEqual(expected, actual)
