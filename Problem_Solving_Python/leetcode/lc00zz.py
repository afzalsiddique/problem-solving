from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Literal; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Di(defaultdict):
    def __missing__(self, key): return key
class Solution: # bfs
    # https://www.youtube.com/watch?v=R58Q0J52qzI
    def numBusesToDestination(self, routes: List[List[int]], src: int, target: int) -> int:
        def performOperation(op:Literal['!','|','&'],li:List[bool]):
            return op
        performOperation('3',[])



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().numBusesToDestination( [[1,2,7],[3,6,7]],  1,  6))
    def test02(self):
        self.assertEqual(-1, get_sol().numBusesToDestination( [[7,12],[4,5,15],[6],[15,19],[9,12,13]],  15,  12))
    def test03(self):
        self.assertEqual(1, get_sol().numBusesToDestination( [[35,38],[10,37,38],[10,28,37]], 37, 28))
    def test04(self):
        self.assertEqual(1, get_sol().numBusesToDestination( [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]], 37, 28))
    def test05(self):
        self.assertEqual(0, get_sol().numBusesToDestination( [[1,7],[3,5]], 5, 5))
    def test06(self):
        self.assertEqual(-1, get_sol().numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]], 7, 47))
