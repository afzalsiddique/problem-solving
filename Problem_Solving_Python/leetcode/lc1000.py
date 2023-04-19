from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=r83itwwSsEQ
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache
        def dp(i,j):
            length = j-i+1
            # if length==k: return pre[j+1]-pre[i]
            if length<k: return 0
            ans=float('inf')
            for mid in range(i,j,k-1):
                ans=min(ans,dp(i,mid)+dp(mid+1,j))
            if (length-1)%(k-1)==0:
                ans+=pre[j+1]-pre[i]
            return ans

        n=len(stones)
        pre=[0]+list(accumulate(stones))
        if (n-1)%(k-1): return -1
        return dp(0,n-1)
class Solution2:
    # tle
    def mergeStones(self, stones: List[int], k: int) -> int:
        INVALID=-1
        def isSelected(mask:tuple,i:int):
            li = list(mask)
            return li[i]
        def allSelected(mask:tuple):
            li = list(mask)
            return all(x for x in li)
        def selectKItems(start:int,mask:tuple,nums:tuple[int]):
            n=len(nums)
            if not start+k<=n: return INVALID,0
            cost=0
            for i in range(start,start+k):
                if isSelected(mask,i): return INVALID,0
                cost+=nums[i]
            li=list(mask)
            for _ in range(k):
                li.pop(start)
            li.insert(0,0)
            return tuple(li),cost
        @cache
        def dfs(mask:tuple,nums:tuple[int]):
            if not nums: return 0
            if len(nums)==1: return 0
            if allSelected(mask):
                return 0
            ans=float('inf')
            for i in range(n-k+1):
                new_mask,cost = selectKItems(i,mask,nums)
                if new_mask==INVALID: continue
                new_nums = nums[:i]+(cost,)+nums[i+k:]
                ans=min(ans,cost+dfs(new_mask,new_nums))
            return ans

        n=len(stones)
        if n<k: return 0
        tmp=n
        while tmp>k:
            tmp=tmp-(k-1)
        if tmp!=k and tmp!=0: return -1
        selected=tuple([0]*n)
        return dfs(selected,tuple(stones))

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(20, get_sol().mergeStones(stones = [3,2,4,1], k = 2))
    def test2(self):
        self.assertEqual(-1, get_sol().mergeStones(stones = [3,2,4,1], k = 3))
    def test3(self):
        self.assertEqual(25, get_sol().mergeStones(stones = [3,5,1,2,6], k = 3))
    def test4(self):
        self.assertEqual(14, get_sol().mergeStones(stones = [3,2,4], k = 2))
    def test5(self):
        self.assertEqual(0, get_sol().mergeStones([1], 2))
    def test6(self):
        self.assertEqual(1957, get_sol().mergeStones([69,39,79,78,16,6,36,97,79,27,14,31,4], 2))
    def test7(self):
        self.assertEqual(4517, get_sol().mergeStones([95,54,31,48,44,96,99,20,51,54,18,85,25,84,91,48,40,72,22], 2))
    def test8(self):
        self.assertEqual(3334, get_sol().mergeStones([16,43,87,30,4,98,12,30,47,45,32,4,64,14,24,84,86,51,11,22,4], 2))
    # def test9(self):
    #     self.assertEqual(25, get_sol().mergeStones(stones = [3,5,1,2], k = 3))
    # def test10(self):
    #     self.assertEqual(25, get_sol().mergeStones(stones = [5,1,2,6], k = 3))
    # def test7(self):
    # def test8(self):

    # def turnOn(mask:int,i:int): return mask|(1<<i)
    # def isSelected(mask:int,i:int): return mask&(1<<i)
    # def allSelected(mask, n): return mask == ((1 << n) - 1)
    # def selectKItems(start:int,mask:int):
    #     if not start+k<=n: return INVALID,0
    #     cost=0
    #     for i in range(start,start+k):
    #         if isSelected(mask,i): return INVALID,0
    #         mask =turnOn(mask,i)
    #         cost+=stones[i]
    #     return mask,cost
