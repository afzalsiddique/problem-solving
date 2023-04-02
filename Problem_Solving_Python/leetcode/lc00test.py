from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    # https://www.youtube.com/watch?v=r83itwwSsEQ
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache
        def dp(i,j):
            if j-i+1==k:
                return pre[j+1]-pre[i]
            if j-i+1<k:
                return 0
            ans=float('inf')
            for mid in range(i,j,k-1):
                ans=min(ans,dp(i,mid)+dp(mid+1,j))
            l=j-i+1
            # if (l-1)%(k-1)==0:
            ans+=pre[j+1]-pre[i]
            return ans

        n=len(stones)
        pre=[0]+list(accumulate(stones))
        if (n-1)%(k-1): return -1
        return dp(0,n-1)

class Correct:
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache
        def dp(i,j):
            if j-i+1==k:
                return pre[j+1]-pre[i]
            if j-i+1<k:
                return 0
            ans=float('inf')
            for mid in range(i,j,k-1):
                ans=min(ans,dp(i,mid)+dp(mid+1,j))
            l=j-i+1
            if (l-1)%(k-1)==0:
                ans+=pre[j+1]-pre[i]
            return ans

        n=len(stones)
        pre=[0]+list(accumulate(stones))
        if (n-1)%(k-1): return -1
        return dp(0,n-1)

class Tester(unittest.TestCase):
    def test01(self):
        a=[3,5,1,2,6],  3
        self.assertEqual(Correct().mergeStones(*a), Solution().mergeStones(*a))
