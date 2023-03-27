from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        def backtrack(i,prevMax):
            if i==n:
                return 0

            # maxx=float('-inf')
            res=0
            for j in range(i,n):
                # maxx=max(maxx,arr[i])
                tmp=arr[i:j+1]
                maxx=max(arr[i:j+1])
                if arr[i]<prevMax: continue
                res=max(res,1+backtrack(i+1,maxx))
            return res

        return backtrack(0,float('-inf'))

class Correct:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)

        max_left=[-1]*n
        max_left[0]=arr[0]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],arr[i])

        min_right=[-1]*n
        min_right[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            min_right[i]=min(min_right[i+1],arr[i])

        res=1
        for i in range(n-1):
            if max_left[i]<=min_right[i+1]:
                res+=1
        return res

class Tester(unittest.TestCase):
    def test01(self):
        a = [2,1,4]
        self.assertEqual(Correct().maxChunksToSorted(a), Solution().maxChunksToSorted(a))
