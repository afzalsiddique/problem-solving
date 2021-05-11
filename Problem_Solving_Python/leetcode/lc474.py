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
    # time O(kl + kmn),
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def counter(s):
            zero,one=0,0
            for c in s:
                if c=='0': zero+=1
                else: one+=1
            return (zero,one)

        li=[]
        for s in strs:
            li.append(counter(s))
        dp = {}

        def helper(i,zeros,ones):
            if i==len(strs): return 0
            if (i,zeros,ones) in dp: return dp[(i,zeros,ones)]
            zero,one=li[i][0],li[i][1]
            select=0
            if zeros>=zero and ones>=one:
                select=1+helper(i+1,zeros-zero,ones-one)
            do_not_select = helper(i+1,zeros,ones)
            ans = max(select,do_not_select)
            dp[(i,zeros,ones)] = ans
            return ans

        # def helper(i,zeros,ones):
        #     if i==len(strs): return 0
        #     if (i,zeros,ones) in dp: return dp[(i,zeros,ones)]
        #     zero,one=li[i][0],li[i][1]
        #     if zeros>=zero and ones>=one:
        #         select=helper(i+1,zeros-zero,ones-one)
        #         do_not_select = helper(i+1,zeros,ones)
        #         ans = max(select+1,do_not_select)
        #     else:
        #         do_not_select = helper(i+1,zeros,ones)
        #         ans = do_not_select
        #     dp[(i,zeros,ones)] = ans
        #     return ans


        return helper(0,m,n)

class tester(unittest.TestCase):
    def test1(self):
        strs = ["10","0001","111001","1","0"]
        m = 5
        n = 3
        Output= 4
        self.assertEqual(Output,Solution().findMaxForm(strs,m,n))
    def test2(self):
        strs = ["10","0","1"]
        m = 1
        n = 1
        Output= 2
        self.assertEqual(Output,Solution().findMaxForm(strs,m,n))
    def test03(self):
        strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
        m = 9
        n = 80
        Output= 17
        self.assertEqual(Output,Solution().findMaxForm(strs,m,n))