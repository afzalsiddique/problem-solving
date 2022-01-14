import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/140541/Clear-explanation-easy-to-understand-C++-:-4ms-beat-100
class Solution:
    def canPartitionKSubsets(self, A: List[int], k: int) -> bool:
        def put(index): # dfs
            if index==len(A): return True
            seen=set()
            for i in range(k):
                if buckets[i]+A[index]>target: continue
                if buckets[i] in seen: continue # optimization
                seen.add(buckets[i])
                buckets[i]+=A[index]
                if put(index+1):
                    return True
                buckets[i]-=A[index]
            return False

        A.sort(reverse=True) # optimization
        summ=sum(A)
        target=summ//k
        if len(A) < k or sum(A) % k != 0 or max(A) > target:
            return False
        buckets=[0]*k
        return put(0)

class Solution9:
    # tle
    # time O(k*2^n)
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        vis=set()
        def divide_k_equal_subset(k, cur_sum):
            if k==1: return True
            if cur_sum==target:
                return divide_k_equal_subset(k - 1, 0)
            if cur_sum>target:
                return False
            for i in range(n):
                if i in vis: continue
                vis.add(i)
                if divide_k_equal_subset(k,cur_sum+nums[i]):
                    return True
                vis.remove(i)
            return False

        summ = sum(nums)
        target=summ//k
        if summ%k!=0: return False
        for num in nums:
            if num>target: return False
        return divide_k_equal_subset(k,0)

# tle
class Solution8:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def helper(k,cur_sum,next_idx):
            if k==self.k: return True
            if cur_sum and cur_sum%self.target_sum==0: return helper(k+1,0,0)
            if cur_sum>self.target_sum*(k+1): return False
            for i in range(next_idx,len(nums)):
                if not visited[i]:
                    visited[i]=True
                    if helper(k,cur_sum+nums[i],i+1):
                        return True
                    visited[i]=False
            return False
        self.total,max_num = sum(nums),max(nums)
        if self.total%k or max_num>self.total//k: return False
        visited = [False for _ in range(len(nums))]
        self.target_sum = self.total//k
        self.k=k
        return helper(0,0,0)

# same as solution1 but with bit masking
# time O(k*2^n)
# tle
class Solution3:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def selectItem(items, itemNo):
            return items | (1<<itemNo)
        def selected(items, itemNo):
            temp = items & (1<<itemNo)
            if temp==0:
                return False
            return True
        def helper(k,items,cur_sum,next_idx):
            if k==0: return True
            if cur_sum==self.target_sum: return helper(k-1,items,0,0)
            if cur_sum>self.target_sum: return False
            for i in range(next_idx,len(nums)):
                if not selected(items,i):
                    items_before = items
                    items = selectItem(items, i)
                    if helper(k,items,cur_sum+nums[i],i+1):
                        return True
                    items = items_before # backtracking
            return False

        total,max_num = sum(nums),max(nums)
        if total%k or max_num>total//k: return False
        self.target_sum = total//k
        return helper(k,0,0,0)

class Solution4:
    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/480707/C%2B%2B-DP-bit-manipulation-in-20-lines
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        summ = sum(nums)
        if summ % k: return False
        tar = summ//k
        for mask in range(1<<n):
            if dp[mask] == -1: # states that were not calculated because sum of included items crosses the target
                continue
            for i in range(n):
                if not (mask&(1<<i)) and dp[mask]+nums[i] <= tar:
                    dp[mask|(1<<i)] = (dp[mask]+nums[i]) % tar

        return dp[(1<<n)-1] == 0


class Solution5:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tsum = sum(nums)
        n = len(nums)

        def go(i, mask, k, csum):
            if k==1:
                return True
            if csum == tsum:
                return go(0, mask, k-1, 0)
            elif csum > tsum:
                return False

            for j in range(i, n):
                if not (mask&(1<<j)):
                    if go(j, mask|(1<<j), k, csum+nums[j]):
                        return True
            return False

        if tsum%k!=0:
            return False
        tsum/=k
        return go(0, 0, k, 0)
class Solution6:
    def canPartitionKSubsets(self,nums: List[int]):
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        summ = sum(nums)
        if summ % 3: return False
        tar = summ//3
        for mask in range(1<<n):
            if dp[mask] == -1: # states that were not calculated because sum of included items crosses the target
                continue
            for i in range(n):
                if not (mask&(1<<i)) and dp[mask]+nums[i] <= tar:
                    dp[mask|(1<<i)] = (dp[mask]+nums[i]) % tar

        return dp[(1<<n)-1] == 0

class Solution7:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        for _ in range(k):
            possible, item_indices = self.canPartitionKSubsetsUtility(nums, k)
            if not possible:
                return False
            for iindex in item_indices:
                nums.pop(iindex)
            k -= 1
        return True

    def canPartitionKSubsetsUtility(self, nums: List[int], k: int):
        if sum(nums) % k:
            return False, []
        n = len(nums)
        SUMM = sum(nums) // k
        numbers = [0]
        for num in nums:
            numbers.append(num)  # converting to 1 based indexing
        dp = [[False] * (SUMM + 1) for _ in range(n + 1)]
        for row in dp:
            row[0] = True
        for i in range(1, n + 1):
            for j in range(1, SUMM + 1):
                item_not_included = dp[i - 1][j]
                if j >= numbers[i] and dp[i - 1][j - numbers[i]]:
                    item_included = True
                else:
                    item_included = False
                if item_included or item_not_included:
                    dp[i][j] = True
        item_indices = []
        if not dp[n][SUMM]:
            return dp[n][SUMM], item_indices
        i, j = n, SUMM
        while i != 0 or j != 0:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                item_indices.append(i - 1)  # item_indices are 0 based
                i, j = i - 1, j - numbers[i]
        return dp[n][SUMM], item_indices



class tester(unittest.TestCase):
    def test00(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([5,3,2,5], 3))
    def test01(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], 4))
    def test02(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([4,5,1,1,1,1,1,1], 3))
    def test03(self):
        self.assertEqual(False, get_sol().canPartitionKSubsets([5, 7, 3], 3))
    def test041(self):
        self.assertEqual(False, get_sol().canPartitionKSubsets([3,4,5], 2))
    def test04(self):
        self.assertEqual(False, get_sol().canPartitionKSubsets([2,2,2,2,3,4,5], 4))
    def test05(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([5,4,2,2,4,3], 2))
    def test06(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([4,4,4,4], 4))
    def test07(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([6,3,1,3,3,2,1,11,3,2,1,2,6,4], 4))
    def test08(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    def test09(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([4,4,4,4], 2))
    def test10(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([1,5,11,5], 2))
    def test11(self):
        self.assertEqual(False, get_sol().canPartitionKSubsets([1,2,3,4], 3))
    def test12(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))
    def test13(self):
        self.assertEqual(False, get_sol().canPartitionKSubsets([2,2,2,2,2,2,2,2,2,2,2,2,2,3,3], 8))
    def test14(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3], 15))
    def test15(self):
        self.assertEqual(True, get_sol().canPartitionKSubsets([4,4,4,6,1,2,2,9,4,6], 3))