from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def dp(i,tall_plus_small,diff,t,s):
            nonlocal res
            # if t==(2, 3, 5) and s==(4,):
            if t==(2,):
                print('hey')
            taller=list(t) if sum(t)>sum(s) else list(s)
            shorter=list(t) if sum(t)<sum(s) else list(s)
            if diff==0:
                res=max(res,tall_plus_small//2)
            if i==n:
                return
            small=(tall_plus_small-diff)//2
            tall=small+diff
            print('tall:',tall,'small:',small,'diff:',diff)
            print(t,s,end='\n\n')
            taller=tuple(taller+[rods[i]])
            shorter=tuple(shorter)
            add_to_tall=dp(i+1,tall+small+rods[i],tall+rods[i]-small,taller,shorter)


            new_tall=max(tall,small+rods[i])
            new_short=min(tall,small+rods[i])
            taller=list(t) if sum(t)>(sum(s)+rods[i]) else list(s)+[rods[i]]
            shorter=list(t) if sum(t)<(sum(s)+rods[i]) else list(s)+[rods[i]]
            add_to_short=dp(i+1, new_tall+new_short,new_tall-new_short,tuple(taller),tuple(shorter))


            taller=list(t) if sum(t)>sum(s) else list(s)
            shorter=list(t) if sum(t)<sum(s) else list(s)
            nothing=dp(i+1,tall_plus_small,diff,tuple(taller),tuple(shorter))

            return

        n=len(rods)
        res=float('-inf')
        dp(0,0,0,tuple([]),tuple([]))
        return res

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
    def test7(self):
        self.assertEqual(5, get_sol().tallestBillboard([1,2,5,3]))
    # def test8(self):
