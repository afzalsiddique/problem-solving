from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
def solution(A,x,y):
    # if y<=x: return takeOnlyY(A,x,y)
    if y<=x: return takeY(A,x,y)
    A.sort()
    n=len(A)
    cost=n*x
    surplus=0
    res=cost
    left,right=0,n-1
    while left<right:
        if A[left]<=surplus:
            surplus-=A[left]
            cost-=x
            res=min(res,cost)
            left+=1
            continue
        surplus+=A[right]
        cost+=y-x
        right-=1
    return res
def takeY(A,x,y):
    A.sort(reverse=True)
    total=sum(A)
    current=0
    cost=0
    i=0
    while current<total:
        current+=2*A[i]
        cost+=y
    return cost

def takeOnlyY(A, x, y):
    A.sort()
    n=len(A)
    cost=n*y
    surplus=sum(A)
    left=0
    while left<n and surplus>=2*A[left]:
        surplus-=2*A[left]
        left+=1
        cost-=y
    return cost


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,solution([1,2,5,6],2,1))
    def test02(self):
        self.assertEqual(7,solution([5,3,8,3,2],2,5))
    def test03(self):
        self.assertEqual(12,solution([4,2,7],4,100))
    def test04(self):
        self.assertEqual(8,solution([2,2,1,2,2],2,3))
    def test05(self):
        self.assertEqual(4,solution([4,1,5,3],5,2))
    def test06(self):
        self.assertEqual(10,solution([1,1,1,1,1],2,5))
    def test07(self):
        self.assertEqual(1,solution([1,1,1,3],3,1))
    def test08(self):
        self.assertEqual(1,solution([1,1,1,3],3,1))
    def test09(self):
        self.assertEqual(2,solution([4,5],1,100))
    def test10(self):
        self.assertEqual(1,solution([4,5],100,1))
