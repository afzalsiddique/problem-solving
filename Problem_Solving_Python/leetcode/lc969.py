import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        def reverse(right):
            left=0
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        if arr==sorted(arr): return []
        res=[]
        right=n
        while right>0:
            idx = arr.index(right)
            reverse(idx)
            reverse(right-1)# -1 because inclusive
            res.append(idx+1)
            res.append(right)
            right-=1
        return res

class tester(unittest.TestCase):
    def test01(self):
        arr = [3,2,4,1]
        Output= [4,2,4,3]
        self.assertEqual(Output, get_sol().pancakeSort(arr))
    def test02(self):
        arr = [1,2,3]
        Output= []
        self.assertEqual(Output, get_sol().pancakeSort(arr))