import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,k):
            if n==0: return 0
            parent = helper(n-1,k//2)
            if k%2==0: # left child
                if parent==1: return 1
                else: return 0
            else: # right child
                if parent == 1: return 0
                else: return 1

        return helper(n-1,k-1)

class Solution2:
    # tle
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(li):
            if len(li)==1:
                if li[0]== '0': return ['0','1']
                else: return ['1','0']
            res = []
            for i in range(len(li)):
                res.extend(helper(li[i]))
            return res

        ans = ['0']
        for _ in range(n - 1):
            ans = helper(ans)
        return int(ans[k - 1])


class tester(unittest.TestCase):
    def test1(self):
        n = 1
        k = 1
        Output= 0
        self.assertEqual(Output,get_sol().kthGrammar(n,k))
    def test2(self):
        n = 2
        k = 1
        Output= 0
        self.assertEqual(Output,get_sol().kthGrammar(n,k))
    def test3(self):
        n = 2
        k = 2
        Output= 1
        self.assertEqual(Output,get_sol().kthGrammar(n,k))
    def test4(self):
        n = 3
        k = 1
        Output= 0
        self.assertEqual(Output,get_sol().kthGrammar(n,k))
    def test5(self):
        n = 30
        k = 434991989
        Output= 0
        self.assertEqual(Output,get_sol().kthGrammar(n,k))