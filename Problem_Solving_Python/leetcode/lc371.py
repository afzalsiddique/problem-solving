from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # wrong
    def getSum(self, a: int, b: int) -> int:
        a=bin(a)[2:]
        b=bin(b)[2:]
        maxx=max(len(a),len(b))
        a=(maxx-len(a))*'0'+a
        b=(maxx-len(b))*'0'+b
        a=list(map(int,a))
        b=list(map(int,b))
        carry=0
        res=[]
        for i in range(maxx-1,-1,-1):
            x=a[i]^b[i]^carry
            res.append(x)
            carry=a[i] and b[i] or b[i] and carry or a[i] and carry
        if carry:
            res.append(carry)
        res.reverse()
        res=list(map(str,res))
        res=''.join(res)
        return int(res,2)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().getSum(1,2))
    def test02(self):
        self.assertEqual(5, get_sol().getSum(2,3))
    def test03(self):
        self.assertEqual(0, get_sol().getSum(-1, 1))
    # def test04(self):
    # def test05(self):
    # def test06(self):
