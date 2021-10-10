import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def calc(index):
            if index==len(ans):
                return True
            if ans[index]!=0: return calc(index+1)
            else:
                for i in range(n,0,-1): # start from n. The first valid sequence is the ans.
                    if i in visited: continue
                    visited.add(i)
                    ans[index]=i
                    if i==1:
                        if calc(index+1): return True
                    elif index+i<len(ans) and ans[index+i]==0:
                        ans[i+index]=i
                        if calc(index+1): return True
                        ans[index+i]=0

                    ans[index]=0
                    visited.remove(i)
            return False

        ans = [0]*(n*2-1)
        visited=set()
        count = Counter()
        for i in range(1,n+1):
            count[i] = 2 if i!=1 else 1

        calc(0)
        return ans

class MyTestCase(unittest.TestCase):
    def test1(self):
        n=12
        Output= [12,10,11,7,5,3,8,9,3,5,7,10,12,11,8,6,9,2,4,2,1,6,4]
        self.assertEqual(Output, get_sol().constructDistancedSequence(n))
    def test2(self):
        n=11
        Output = [11,9,10,6,4,1,7,8,4,6,9,11,10,7,5,8,2,3,2,5,3]
        self.assertEqual(Output, get_sol().constructDistancedSequence(n))
    def test3(self):
        n=3
        Output = [3,1,2,3,2]
        self.assertEqual(Output, get_sol().constructDistancedSequence(n))
    def test4(self):
        n=5
        Output = [5,3,1,4,3,5,2,4,2]
        self.assertEqual(Output, get_sol().constructDistancedSequence(n))
    def test5(self):
        n=1
        Output = [1]
        self.assertEqual(Output, get_sol().constructDistancedSequence(n))
    # def test6(self):
    # def test7(self):

