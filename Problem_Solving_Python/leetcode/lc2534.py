from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # enter_q and exit_q
    # range(2*n)
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        ENTER,EXIT='ENTER','EXIT'
        n=len(arrival)
        enter_q=deque((t,i) for i,t in enumerate(arrival) if state[i]==0)
        exit_q=deque((t,i) for i,t in enumerate(arrival) if state[i]==1)
        last_usage=EXIT
        res=[None]*n
        for time in range(2*n): ### RANGE(2*n)
            t,i=None,None
            if last_usage==ENTER and enter_q and enter_q[0][0]<=time:
                t,i=enter_q.popleft()
                last_usage=ENTER
            elif last_usage==EXIT and exit_q and exit_q[0][0]<=time:
                t,i=exit_q.popleft()
                last_usage=EXIT
            if (t,i)==(None,None):
                if enter_q and enter_q[0][0]<=time:
                    t,i=enter_q.popleft()
                    last_usage=ENTER
            if (t,i)==(None,None):
                if exit_q and exit_q[0][0]<=time:
                    t,i=exit_q.popleft()
                    last_usage=EXIT
            if (t,i)==(None,None):
                last_usage=EXIT
                continue
            res[i]=time
        return res





class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,1,2,4], get_sol().timeTaken([0,1,1,2,4], [0,1,0,0,1]))
    def test2(self):
        self.assertEqual([0,2,1], get_sol().timeTaken([0,0,0], [1,0,1]))
    def test3(self):
        self.assertEqual([3,6,4,7,5,8], get_sol().timeTaken([3,3,4,5,5,5], [1,0,1,0,1,0]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
