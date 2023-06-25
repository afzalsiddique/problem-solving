from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution3()
class Solution6:
    # TLE. basic dp
    def tallestBillboard(self, nums):
        @cache
        def dp(i,s1,s2):
            if i==n:
                if s1==s2: return s1
                return float('-inf')
            option1=dp(i+1,s1,s2)
            option2=dp(i+1,s1+nums[i],s2)
            option3=dp(i+1,s1,s2+nums[i])
            return max(option1,option2,option3)

        n=len(nums)
        return dp(0,0,0)
class Solution:
    # Official Solution 2
    # https://leetcode.com/problems/tallest-billboard/solution/
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[taller-shorter]=taller
        dp={0:0}
        for r in rods:
            # option1: do not add rod any ends. copy dp
            dpCopy=defaultdict(lambda :float('-inf'))
            for k,v in dp.items(): dpCopy[k]=v
            # alternative. Instead of using dpCopy use a list. I don't think option1 is necessary
            # li = list(dp.items())
            # for diff,taller in li:
            for diff,taller in dp.items():
                shorter=taller-diff
                # option2: add rod the taller end
                newDiff1=diff+r
                newTaller1=taller+r
                dpCopy[newDiff1]=max(dpCopy[newDiff1],newTaller1)
                # option3: add rod the shorter end
                newDiff2=abs(shorter+r-taller)
                newTaller2=max(taller,shorter+r)
                dpCopy[newDiff2]=max(dpCopy[newDiff2],newTaller2)
            dp=dpCopy

        return dp[0]
class Solution3:
    # https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
    def tallestBillboard(self,rods):
        # dp[taller-shorter]=shorter
        dp = defaultdict(int)
        dp[0]=0
        for x in rods:
            # init state
            # ------|----- d -----|      # tall side
            # - y --|                    # low  side
            dpCopy=defaultdict(lambda :float('-inf'))
            for k,v in dp.items(): dpCopy[k]=v
            for d, y in dp.items():
                # put x to tall side
                # ------|----- d -----|---- x --|
                # - y --|
                dpCopy[d+x] = max(dpCopy[d+x], y )

                # put x to low side
                if d >= x:
                    # ------|----- d -----|
                    # - y --|---- x ---|
                    dpCopy[d-x] = max(dpCopy[d-x], y+x)
                else:
                    # ------|----- d -----|
                    # - y --|-------- x --------|
                    dpCopy[x-d] = max(dpCopy[x-d], y+d)
            dp=dpCopy
        return dp[0]
class Solution2:
    # tle. dfs
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(i,left,right,remain):
            nonlocal res
            if left==right:
                res=max(res,left)
            if i==n:
                return
            if left+right+remain<2*res:
                return
            if abs(right-left)>remain:
                return
            helper(i+1,left+rods[i],right,remain-rods[i]) # use it for left support
            helper(i+1,left,right+rods[i],remain-rods[i]) # use it for right support
            helper(i+1,left,right,remain) # do not use it for any supports

        n=len(rods)
        res=0
        helper(0,0,0,sum(rods))
        return res
class Solution7:
    # tle
    def tallestBillboard(self, rods: List[int]) -> int:
        def isOn(mask:int,i:int):
            return mask&(1<<i)
        def getNums(mask:int):
            li=[]
            for i in range(n):
                if isOn(mask,i):
                    li.append(rods[i])
            return li

        n=len(rods)
        res=float('-inf')
        for mask in range(2**n-1,-1,-1):
            nums=getNums(mask)
            if self.canPartition(nums):
                res=max(res,sum(nums)//2)
        return res


    def canPartition(self, nums: List[int]) -> bool: # leetcode 416
        @cache
        def helper(start,target):
            if target==0:
                return True
            for i in range(start,n):
                if helper(i+1,target-nums[i]):
                    return True
            return False

        n=len(nums)
        if sum(nums)%2: return False
        return helper(0,sum(nums)//2)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, get_sol().tallestBillboard([1,2,3,6]))
    def test2(self):
        self.assertEqual(10, get_sol().tallestBillboard([1,2,3,4,5,6]))
    def test3(self):
        self.assertEqual(0, get_sol().tallestBillboard([1,2]))
    def test4(self):
        self.assertEqual(1023, get_sol().tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))
    def test5(self):
        self.assertEqual(6, get_sol().tallestBillboard([3,4,3,3,2]))
    def test6(self):
        self.assertEqual(756, get_sol().tallestBillboard([140,138,133,162,145,164,145,166,145,154,158]))
    # def test7(self):
    # def test8(self):
