from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(a,b,c): return solution(a,b,c)
def solution(A, B, C):
    def conforms(X,A): # x conforms A
        for i in range(30):
            a=(A>>i) & 1
            x=(X>>i) & 1
            if a==1 and x==0:
                return False
        return True
    def conformsAny(X): return any(conforms(X,a) for a in [A,B,C])

    res=0
    for i in range(2**10):
        res+=conformsAny(i)
    return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual( 8,get_sol(1073741727,1073741631,1073741679))
    # def test02(self):
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
