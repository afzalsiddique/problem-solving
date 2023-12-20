from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(*args): return Solution().isRobotBounded(*args)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        n=len(instructions)
        x,y=0,0
        dx,dy=0,1
        for i in range(4*n):
            if instructions[i%n]=='G':
                x+=dx
                y+=dy
            elif instructions[i%n]=='L':
                dx,dy=dy*(-1),dx
            else:
                dx,dy=dy,dx*(-1)
        return (x,y)==(0,0)



Cases=[
    "GGLLGG",
    "GG",
    "GL"
]
Expected=[True,False,True]
PARAMETERS=1

class MyTestCase(unittest.TestCase):
    def test00(self):
        testNo=0
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test01(self):
        testNo=1
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    def test02(self):
        testNo=2
        self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test03(self):
    #     testNo=3
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test04(self):
    #     testNo=4
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test05(self):
    #     testNo=5
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


