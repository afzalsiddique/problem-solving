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
    # https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/864332/Minimax-with-DP-in-Python-(with-recursion-tree-plotted)
    # https://www.youtube.com/watch?v=qBgxeaxX3l8
    def getMoneyAmount(self, n: int) -> int:
        dp={}
        def helper(lo,hi):
            if lo>=hi: return 0 # it "lo>=hi" and not "lo>hi". because if there is only one number in the range
            if (lo,hi) in dp: return dp[(lo,hi)]
            ans=float('inf')
            for x in range(lo,hi+1): # including hi
                temp = x+max(helper(lo,x-1),helper(x+1,hi))
                ans = min(ans,temp)
            dp[(lo,hi)]=ans
            return ans
        return helper(1,n)

class mytestcase(unittest.TestCase):
    def test01(self):
        n=10
        Output= 16
        self.assertEqual(Output,get_sol().getMoneyAmount(n))
