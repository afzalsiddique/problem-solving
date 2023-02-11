from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution3()
class Solution4:
    # bfs. Node j is connected to node i via an edge if and only if either j = i + (a perfect square number)
    def numSquares(self, n: int) -> int:
        perfectSqs=[]
        i=1
        while i*i<=n:
            perfectSqs.append(i*i)
            i+=1
        if perfectSqs[-1]==n: return 1
        visited = [False]*(n+1)
        q = deque(perfectSqs)

        res=1
        while q:
            res+=1
            for _ in range(len(q)):
                x = q.popleft()
                for sq in perfectSqs:
                    if x+sq==n: return res
                    elif x+sq<n and not visited[x+sq]:
                        q.append(x+sq)
                        visited[x+sq]=True
                    elif x+sq>n: break
# https://www.youtube.com/watch?v=1xfx6M_GqFk
class Solution3:
    # dp. not good enough
    def numSquares(self, n: int) -> int:
        @cache
        def func(n):
            if n<=3: return n
            res=float('inf')
            i=1
            while i*i<=n:
                res=min(res,func(n-i*i))
                i+=1
            return res+1

        return func(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        dp[0] = float('inf')
        for num in range(4, n + 1):
            minn = float('inf')
            i = 1
            while i * i <= num:
                if i * i == num:
                    minn = 1
                else:
                    minn = min(minn, dp[num - i * i] + 1)
                i += 1
            dp[num] = minn
        return dp[-1]


class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        for num in range(1, n + 1):
            i = 1
            while i * i <= num:
                sq = i*i
                dp[num] = min(dp[num], 1+dp[num-sq])
                i += 1
        return dp[-1]
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().numSquares(12))
    def test02(self):
        self.assertEqual(2, get_sol().numSquares(13))
    def test03(self):
        self.assertEqual(1, get_sol().numSquares(1))
    def test04(self):
        self.assertEqual(1, get_sol().numSquares(4))
    def test05(self):
        self.assertEqual(2, get_sol().numSquares(5))
    def test06(self):
        self.assertEqual(3, get_sol().numSquares(6110))
