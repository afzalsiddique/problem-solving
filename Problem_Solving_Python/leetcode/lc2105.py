import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n=len(plants)
        a,b=capacityA,capacityB
        res=0
        left,right=0,n-1
        while left<=right:
            if left==right:
                if a>b:
                    if a<plants[left]:
                        res+=1
                elif b<plants[right]:
                    res+=1
                break

            while left<right and plants[left]<=a and plants[right]<=b:
                a-=plants[left]
                b-=plants[right]
                left+=1
                right-=1


            if left<right and a<plants[left]:
                res+=1
                a=capacityA
            if left<right and b<plants[right]:
                res+=1
                b=capacityB
        return res



class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minimumRefill(plants = [2,2,3,3], capacityA = 5, capacityB = 5))
    def test2(self):
        self.assertEqual(2, get_sol().minimumRefill(plants = [2,2,3,3], capacityA = 3, capacityB = 4))
    def test3(self):
        self.assertEqual(0, get_sol().minimumRefill(plants = [5], capacityA = 10, capacityB = 8))
    def test4(self):
        self.assertEqual(2, get_sol().minimumRefill(plants = [1,2,4,4,5], capacityA = 6, capacityB = 5))
    def test5(self):
        self.assertEqual(1, get_sol().minimumRefill(plants = [2,2,5,2,2], capacityA = 5, capacityB = 5))
    def test6(self):
        self.assertEqual(0, get_sol().minimumRefill([2,3,3], 5, 5))

    # def test7(self):
