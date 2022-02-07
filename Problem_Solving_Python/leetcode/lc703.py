from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(a,b): return KthLargest(a,b)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq=[float('-inf')]*k
        for x in nums:
            self.add(x)
    def add(self, val: int) -> int:
        heappush(self.pq,val)
        heappop(self.pq)
        # heappushpop(self.pq,val) # one line
        return self.pq[0]
class KthLargest2:
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.pq = []
        for val in nums:
            self.add(val)
    def add(self, val):
        if len(self.pq)<self.k:
            heappush(self.pq, val)
        else:
            if self.pq[0]<val:
                heappop(self.pq)
                heappush(self.pq, val)
        return self.pq[0]

class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='KthLargest': obj = get_sol(input[0],input[1]); outputs.append(None)
            elif cmd=='add': outputs.append(obj.add(input[0]))
        return outputs
    def test01(self):
        commands = ["KthLargest","add","add","add","add","add"]
        inputs=[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
        expected = [None, 4, 5, 5, 8, 8]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
