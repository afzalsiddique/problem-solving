import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pattern_set=set(pattern)
        def filt(x): # filter chars in pattern and upper case chars
            if x in pattern_set or 'A'<=x<'Z':
                return True
            return False
        def is_match(query):
            query=''.join(filter(filt,query))
            i,j=0,0
            if len(pattern)>len(query): return False # optimization
            while i<len(query) and j<len(pattern):
                if query[i]==pattern[j]:
                    i+=1
                    j+=1
                elif 'A'<=query[i]<'Z':
                    return False
                else:
                    i+=1
            while i<len(query):
                if 'A'<=query[i]<'Z':
                    return False
                i+=1
            if i==len(query) and j==len(pattern): return True
            return False


        res=[]
        for query in queries:
            res.append(is_match(query))
        return res

class tester(unittest.TestCase):
    def test_1(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FB"
        Output= [True,False,True,True,False]
        self.assertEqual(Output, get_sol().camelMatch(queries,pattern))
    def test_2(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FoBa"
        Output= [True,False,True,False,False]
        self.assertEqual(Output, get_sol().camelMatch(queries,pattern))
    def test_3(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FoBaT"
        Output= [False,True,False,False,False]
        self.assertEqual(Output, get_sol().camelMatch(queries,pattern))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):