from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            li=list(str(num*(-1)))
            li.sort(reverse=True)
            return (-1)*int(''.join(li))
        li=list(str(num))
        li.sort()
        i=0
        zeros=0
        while i<len(li) and li[i]=='0':
            zeros+=1
            i+=1

        res=[]
        if i<len(li):
            res.append(li[i])
            i+=1
        for _ in range(zeros):
            res.append('0')
        while i<len(li):
            res.append(li[i])
            i+=1
        return int(''.join(res))


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(103, get_sol().smallestNumber(310))
    def test02(self):
        self.assertEqual(-7650, get_sol().smallestNumber(-7605))
    def test03(self):
        self.assertEqual(0, get_sol().smallestNumber(0))
    def test04(self):
        self.assertEqual(101, get_sol().smallestNumber(110))
