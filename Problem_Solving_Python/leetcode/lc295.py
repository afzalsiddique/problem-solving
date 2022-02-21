from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return MedianFinder()
class MaxHeap(list):
    def __init__(self,heapType): # type=1 -> minHeap type=2 -> maxHeap
        super().__init__()
        self.type=heapType
    def topVal(self): return self[0]*self.type
    def push(self, val): heappush(self, val * self.type)
    def heappop(self): return heappop(self)*self.type
    def __repr__(self): return str([x * self.type for x in self])
class MedianFinder:
    def __init__(self):
        self.mxHeap=MaxHeap(-1)
        self.mnHeap=MaxHeap(1)
    def addNum(self, num: int) -> None:
        mn=self.mnHeap
        mx=self.mxHeap
        mx.push(num)
        mn.push(mx.heappop())
        if len(mx)<len(mn): # if total elements is odd mx contains the extra element
            mx.push(mn.heappop())
        return
    def findMedian(self) -> float:
        mn=self.mnHeap
        mx=self.mxHeap
        if len(mx)>len(mn):
            return mx.topVal()
        return (mx.topVal()+mn.topVal())/2
class MedianFinder2:

    def __init__(self):
        self.left = []
        self.right = []

    def balance(self):
        if len(self.left) - len(self.right) == 2:
            heappush(self.right, -heappop(self.left))
        elif len(self.left) - len(self.right) == -2:
            heappush(self.left, -heappop(self.right))

    def addNum(self, num):
        if len(self.left) == 0:
            heappush(self.left, -num)
            return
        if num <= -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2.0
        return -float(self.left[0]) if len(self.left) > len(self.right) else float(self.right[0])



class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MedianFinder': obj = get_sol(); outputs.append(None)
            elif cmd=='addNum': outputs.append(obj.addNum(input[0]))
            elif cmd=='findMedian': outputs.append(obj.findMedian())
        return outputs
    def test01(self):
        commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        inputs=[      [],            [1],      [2],        [],          [3],     []]
        expected = [None, None, None, 1.5, None, 2.0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
        inputs=[[],[40],[],[12],[],[16],[],[14],[],[35],[],[19],[],[34],[],[35],[],[28],[],[35],[],[26],[],[6],[],[8],[],[2],[],[14],[],[25],[],[25],[],[4],[],[33],[],[18],[],[10],[],[14],[],[27],[],[3],[],[35],[],[13],[],[24],[],[27],[],[14],[],[5],[],[0],[],[38],[],[19],[],[25],[],[11],[],[14],[],[31],[],[30],[],[11],[],[31],[],[0],[]]
        expected = [None,None,40.00000,None,26.00000,None,16.00000,None,15.00000,None,16.00000,None,17.50000,None,19.00000,None,26.50000,None,28.00000,None,31.00000,None,28.00000,None,27.00000,None,26.00000,None,22.50000,None,19.00000,None,22.00000,None,25.00000,None,22.00000,None,25.00000,None,22.00000,None,19.00000,None,18.50000,None,19.00000,None,18.50000,None,19.00000,None,18.50000,None,19.00000,None,21.50000,None,19.00000,None,18.50000,None,18.00000,None,18.50000,None,19.00000,None,19.00000,None,19.00000,None,18.50000,None,19.00000,None,19.00000,None,19.00000,None,19.00000,None,19.00000]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)


