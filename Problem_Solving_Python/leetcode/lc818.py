from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/race-car/discuss/123834/JavaC++Python-DP-solution/122557
    def racecar(self, target: int) -> int:
        @cache
        def func(i):
            # dir = change direction
            n=i.bit_length() # we need n steps to reach or pass the target
            if 2**n-1==i: # reach target with n steps
                return n
            option2 = float('inf')
            #        steps   dir    remaining
            option1 = n +     1   + func(2**n-1-i) # moved past the target with n steps. change direction once.
            # for m in range(n): # wrong. m can be equal to n-1. that means we are moving n-1 steps forward and m=n-1 steps backward. resulting in the same position.
            for m in range(n-1):
                #                    steps + dir + steps + dir +          n-1 steps forward      m steps backward
                option2=min(option2, (n-1) +  1  + (m)   +  1  + func(i - (2**(n-1)-1)          + (2**m-1)  )) # move n-1 steps forward and m steps backward. also change dir twice
            return min(option1,option2)

        return func(target)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,get_sol().racecar(3))
    def test2(self):
        self.assertEqual(5,get_sol().racecar(6))
    def test3(self):
        self.assertEqual(39,get_sol().racecar(6102))
    def test4(self):
        self.assertEqual(4,get_sol().racecar(2))
    # def test5(self):
