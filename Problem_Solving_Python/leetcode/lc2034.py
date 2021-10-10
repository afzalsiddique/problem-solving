import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return StockPrice()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
    def topPrice(self): return -self[0][0]
    def topTime(self): return -self[0][1]
    def setTopPrice(self,val): self[0][0]=val*(-1)
    def setTopTime(self, val): self[0][1]= val * (-1)
    def push(self, price, time): heappush(self, [-price, -time])
    def heappop(self): return heappop(self)
class MinHeap(list):
    def __init__(self):
        super().__init__()
    def topPrice(self): return self[0][0]
    def topTime(self): return self[0][1]
    def setTopPrice(self,val): self[0][0]=val
    def setTopTime(self, val): self[0][1]= val
    def push(self, price, time): heappush(self, [price, time])
    def heappop(self): return heappop(self)
class StockPrice:
    def __init__(self):
        self.max_timestamp = 0
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        self.di = {}
    def update(self, timestamp: int, price: int) -> None:
        self.max_timestamp=max(self.max_timestamp,timestamp)
        min_heap,max_heap,di= self.min_heap,self.max_heap,self.di
        if timestamp not in di:
            min_heap.push(price,timestamp)
            max_heap.push(price,timestamp)
            di[timestamp]=price
        else:
            min_heap.push(price,timestamp)
            max_heap.push(price,timestamp)
            di[timestamp]=price

    def current(self) -> int:
        return self.di[self.max_timestamp]

    def maximum(self) -> int:
        min_heap,max_heap,di = self.min_heap,self.max_heap,self.di
        while max_heap.topPrice() != di[max_heap.topTime()]:
            max_heap.heappop()
        return max_heap.topPrice()
    def minimum(self) -> int:
        min_heap,max_heap,di = self.min_heap,self.max_heap,self.di
        while min_heap.topPrice() != di[min_heap.topTime()]:
            min_heap.heappop()
        return min_heap.topPrice()


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='StockPrice':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='update':
                outputs.append(obj.update(input[0],input[1]))
            elif cmd=='current':
                outputs.append(obj.current())
            elif cmd=='maximum':
                outputs.append(obj.maximum())
            elif cmd=='minimum':
                outputs.append(obj.minimum())
        return outputs
    def test_01(self):
        commands = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
        inputs=[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
        expected = [None, None, None, 5, 10, None, 5, None, 2]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

