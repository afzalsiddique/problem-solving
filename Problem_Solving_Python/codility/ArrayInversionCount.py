from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
# performance 80%
class Node:
    def __init__(self, val:int, summ:int):
        self.val=val
        self.summ=summ
        self.dup=1
        self.left=None
        self.right=None
    def __repr__(self): return str(self.val)
def countSmaller(nums: List[int]) -> List[int]:
    def insert(num:int,node:Node,i:int,preSum:int):
        if not node:
            node = Node(num,0)
            res[i]=preSum
        elif node.val==num:
            node.dup+=1
            res[i]=preSum+node.summ
        elif node.val>num:
            node.summ+=1
            node.left=insert(num, node.left, i, preSum)
        else:
            node.right=insert(num,node.right,i,preSum+node.dup+node.summ)
        return node

    n=len(nums)
    res=[0]*n
    root=None
    for i in range(n-1,-1,-1):
        root=insert(nums[i],root,i,0)
    return res
def solution(A):
    res=countSmaller(A)
    return sum(res)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,solution([-1,6,3,4,7,4]))
    def test02(self):
        self.assertEqual(0,solution([]))
    def test03(self):
        self.assertEqual(0,solution(list(range(1000)))) # maximum recursion depth exceeded
    def test04(self):
        self.assertEqual(5050,solution(list(range(1000,-1,-1)))) # maximum recursion depth exceeded
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
