import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    # backtracking
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res,n=set(), len(nums)
        def helper(this_idx, path):
            if len(path)>1:
                res.add(tuple(path[:]))
            for i in range(this_idx,n):
                if not path or nums[i]>=path[-1]:
                    helper(i+1,path+[nums[i]])

        helper(0,[])
        res=list(map(list,res))
        return res
class Solution2:
    # longest increasing subsequence
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        lis = [[] for _ in range(n)]
        for i in range(n):
            lis[i].append(tuple([nums[i]]))
        for i in range(n):
            for j in range(i):
                if nums[j]<=nums[i]:
                    for seq in lis[j]:
                        lis[i].append(seq[:]+tuple([nums[i]]))
        sett = set()
        for li in lis:
            for x in li:
                if len(x)>1:
                    sett.add(x)
        res=list(map(list,sett))
        return res
class mytestcase(unittest.TestCase):
    def test01(self):
        nums = [4,6,7,7]
        Output= [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        self.assertEqual(Output,get_sol().findSubsequences(nums))
    def test1_2(self):
        nums = [4,4,3,2,1]
        Output= [[4,4]]
        self.assertEqual(Output,get_sol().findSubsequences(nums))
