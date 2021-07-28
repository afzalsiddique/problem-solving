import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m= arr[(len(arr)-1)//2]
        i,j=0,len(arr)-1
        while len(arr)-1-j+i<k:
            if abs(arr[i]-m)==abs(arr[j]-m):
                if arr[i]>arr[j]:
                    i+=1
                else:
                    j-=1
            elif abs(arr[i]-m)>abs(arr[j]-m):
                i+=1
            else:
                j-=1
        return arr[:i]+arr[j+1:]
class Solution2:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m= arr[(len(arr)-1)//2]
        arr.sort(key=lambda x:(abs(x-m),x))
        return arr[-k:]

class tester(unittest.TestCase):
    def test_1(self):
        arr = [1,2,3,4,5]
        k = 2
        Output= sorted([5,1])
        self.assertEqual(Output,sorted(get_sol().getStrongest(arr,k)))
    def test_2(self):
        arr = [1,1,3,5,5]
        k = 2
        Output= sorted([5,5])
        self.assertEqual(Output,sorted(get_sol().getStrongest(arr,k)))
    def test_3(self):
        arr = [6,7,11,7,6,8]
        k = 5
        Output= sorted([11,8,6,6,7])
        self.assertEqual(Output,sorted(get_sol().getStrongest(arr,k)))
    def test_4(self):
        arr = [6,-3,7,2,11]
        k = 3
        Output= sorted([-3,11,2])
        self.assertEqual(Output,sorted(get_sol().getStrongest(arr,k)))
    def test_5(self):
        arr = [-7,22,17,3]
        k = 2
        Output= sorted([22,17])
        self.assertEqual(Output,sorted(get_sol().getStrongest(arr,k)))
    # def test_6(self):
