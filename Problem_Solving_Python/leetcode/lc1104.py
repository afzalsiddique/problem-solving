import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ENOUGH=22
        def get_row(n:int):
            if n==1: return 1
            for i in range(2,ENOUGH):
                if 2**(i-1)<=n<2**i: return i

        def get_last_node_from_prev_row(node:int): # as in a complete binary tree without zigzag
            i = get_row(node)
            return 2**(i-1)-1
        def get_first_node_from_next_row(node:int): # as in a complete binary tree without zigzag
            i=get_row(node)
            return 2**i

        res=[]
        res.append(label)
        while label!=1:
            label=label//2
            tmp = label - get_last_node_from_prev_row(label)
            label = get_first_node_from_next_row(label) - tmp
            res.append(label)
        res.reverse()
        return res

class tester(unittest.TestCase):
    def test_1(self):
        label = 14
        Output= [1,3,4,14]
        self.assertEqual(Output, get_sol().pathInZigZagTree(label))
    def test_2(self):
        label = 26
        Output= [1,2,6,10,26]
        self.assertEqual(Output, get_sol().pathInZigZagTree(label))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):