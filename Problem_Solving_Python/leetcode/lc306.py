import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(s,path):
            if not s and len(path)>=3:
                return True
            for i in range(1,len(s)+1):
                first,second = s[:i],s[i:]
                if len(first)>1 and first[0]=='0': continue
                if len(path)<=1:
                    if backtrack(second,path+[first]):
                        return True
                else:
                    if int(first)==int(path[-1])+int(path[-2]):
                        if backtrack(second,path+[first]):
                            return True
            return False

        return backtrack(num,[])
class tester(unittest.TestCase):
    def test01(self):
        Input= "112358"
        Output= True
        self.assertEqual(Output, get_sol().isAdditiveNumber(Input))
    def test02(self):
        Input= "199100199"
        Output= True
        self.assertEqual(Output, get_sol().isAdditiveNumber(Input))
    def test03(self):
        Input= "101"
        Output= True
        self.assertEqual(Output, get_sol().isAdditiveNumber(Input))
