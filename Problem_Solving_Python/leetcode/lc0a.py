from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        start,end=float('inf'),float('-inf')
        pq=[]
        for i in range(n):
            tmp_num=nums[i][0]
            heappush(pq,[tmp_num,i,0])
            start=min(start,tmp_num)
            end=max(end,tmp_num)
        res_start,res_end,res_diff=start,end,end-start
        while pq:
            num,i,j=heappop(pq)
            j+=1
            if j>=len(nums[i]): break
            heappush(pq,[nums[i][j],i,j])

            start=pq[0][0]
            end=max(end,nums[i][j])
            cur_diff=end-start
            if cur_diff<res_diff:
                res_start,res_end=start,end
        return [res_start,res_end]

class Correct:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k=len(nums)
        pq=[]
        cur_max=float('-inf')
        for i in range(k):
            heappush(pq,[nums[i][0],0,i]) # cur_min, idx, row_no
            cur_max=max(cur_max,nums[i][0])

        minn,maxx=float('inf'),float('-inf')
        max_min_diff=float('inf')
        while len(pq)==k:
            cur_min,idx,row_no=heappop(pq)
            if cur_max-cur_min<max_min_diff:
                max_min_diff=cur_max-cur_min
                minn,maxx=cur_min,cur_max
            if idx+1<len(nums[row_no]):
                heappush(pq,[nums[row_no][idx+1],idx+1,row_no])
                cur_max=max(cur_max,nums[row_no][idx+1])

        return [minn,maxx]


class Tester(unittest.TestCase):
    def test01(self):
        nums=[[73],[11,13,76],[15]]
        self.assertEqual(Correct().smallestRange(nums), Solution().smallestRange(nums))
    def test02(self):
        nums=[[73],[11,13,76,79],[31,42,42],[15]]
        self.assertEqual(Correct().smallestRange(nums), Solution().smallestRange(nums))
    def test03(self):
        nums=[[73],[11,13,76,79,90],[31,42,42,57],[13,15],[6,39],[31,32,33],[14,15,15,18,19],[12,20],[64,65],[50,54],[38,38,40],[20,22],[72,74,75],[71,72,72,73],[6,26]]
        self.assertEqual(Correct().smallestRange(nums), Solution().smallestRange(nums))
