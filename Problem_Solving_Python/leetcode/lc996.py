from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# similar to leetcode 47
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        INVALID=-1
        def check(x,y):
            tmp = sqrt(x+y)
            return floor(tmp)==ceil(tmp)
        def backtrack(nums:List[int],last:int):
            if not nums: return 1

            res=0
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                cur=nums[i]
                if last==INVALID:
                    res+=backtrack(nums[:i]+nums[i+1:],cur)
                elif check(last,cur):
                        res+=backtrack(nums[:i]+nums[i+1:],cur)
            return res

        nums.sort()
        return backtrack(nums,INVALID)
class Solution2:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def isSquare(x):
            y=sqrt(x)
            return floor(y)==ceil(y)
        def backtrack(A:List[int],path:List[int]):
            if not A:
                res.append(path)
            for i in range(len(A)):
                if i>0 and A[i]==A[i-1]:
                    continue
                if not path or isSquare(path[-1]+A[i]):
                    backtrack(A[:i]+A[i+1:],path+[A[i]])

        res=[]
        nums.sort()
        backtrack(nums,[])
        return len(res)
class Solution3:
    # tle
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def backtrack(nums:List[int],path:List[int]):
            if not nums:
                for x,y in zip(path,path[1:]):
                    tmp=sqrt(x+y)
                    if floor(tmp)!=ceil(tmp):
                        return 0
                return 1

            res=0
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                res+=backtrack(nums[:i]+nums[i+1:],path[:]+[nums[i]])
            return res

        nums.sort()
        return backtrack(nums,[])

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().numSquarefulPerms([1,17,8]))
    def test02(self):
        self.assertEqual(1, get_sol().numSquarefulPerms([2,2,2]))
    def test03(self):
        self.assertEqual(0, get_sol().numSquarefulPerms([89,72,71,44,50,72,26,79,33,27,84]))
    def test04(self):
        self.assertEqual(1, get_sol().numSquarefulPerms([1,1,8,1,8]))
