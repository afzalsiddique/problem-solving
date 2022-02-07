from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution3()
class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(s:str):
            result = []
            j=0
            i=0
            while i<len(s):
                if i>0 and s[i]!=s[i-1]:
                    result.append(str(i-j) + s[j])
                    j=i
                i+=1
            result.append(str(i-j)+s[j])
            return "".join(result)


        if n==1:return "1"
        temp = '1'
        for i in range(n-1):
            temp = helper(temp)
        return temp


class Solution2:
    def countAndSay(self, n: int) -> str:
        def count(s:str):
            res=[]
            i,j=0,0
            while j<len(s):
                while j<len(s) and s[i]==s[j]:
                    j+=1
                res.append(str(j-i))
                res.append(s[i])
                i=j
            return ''.join(res)

        s='1'
        if n==1: return s
        for _ in range(n-1):
            s=count(s)
        return s


class Solution3:
    # less readable
    def countAndSay(self, n: int) -> str:
        s = "1 "
        result = []
        for _ in range(n-1):
            l,r=0,0
            while s[r]!=' ':
                while s[l]==s[r]:
                    r+=1
                result.append(str(r-l))
                result.append(s[l])
                l=r
            result.append(" ")
            s = "".join(str(x) for x in result)
            result = []
            # print(s)
        return s[:-1]





class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual('1',get_sol().countAndSay(1))
    def test_2(self):
        self.assertEqual('11',get_sol().countAndSay(2))
    def test_3(self):
        self.assertEqual('21',get_sol().countAndSay(3))
    def test_4(self):
        self.assertEqual('1211',get_sol().countAndSay(4))
    def test_5(self):
        self.assertEqual('111221',get_sol().countAndSay(5))
    def test_6(self):
        self.assertEqual('312211',get_sol().countAndSay(6))
