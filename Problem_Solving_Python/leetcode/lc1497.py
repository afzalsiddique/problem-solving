import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        mods=[]
        for i in range(n):
            mods.append(arr[i]%k)
        mods.sort()
        i=0;j=n-1
        while i<n and mods[i]==0:
            i+=1
        if i%2: return False # odd no of zeros
        while i<j:
            if (mods[i]+mods[j])%k: return False
            i+=1
            j-=1
        return True

class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [1,2,3,4,5,10,6,7,8,9]; k = 5
        Output= True
        self.assertEqual(Output,get_sol().canArrange(arr,k))
    def test2(self):
        arr = [1,2,3,4,5,6]; k = 7
        Output= True
        self.assertEqual(Output,get_sol().canArrange(arr,k))
    def test3(self):
        arr = [1,2,3,4,5,6]; k = 10
        Output= False
        self.assertEqual(Output,get_sol().canArrange(arr,k))
    def test4(self):
        arr = [-10,10]; k = 2
        Output= True
        self.assertEqual(Output,get_sol().canArrange(arr,k))
    def test5(self):
        arr = [-1,1,-2,2,-3,3,-4,4]; k = 3
        Output= True
        self.assertEqual(Output,get_sol().canArrange(arr,k))
