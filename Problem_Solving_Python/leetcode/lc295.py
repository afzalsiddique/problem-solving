import unittest
from heapq import *


class MedianFinder:

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

# Solution 2
class MinHeap:
    def __init__(self): self.h = []
    def push(self, x): heappush(self.h, x)
    def pop(self): return heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeapObj:
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)

class MaxHeap(MinHeap):
    def push(self, x): heappush(self.h, MaxHeapObj(x))
    def pop(self): return heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val
class MedianFinder_:

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def balance(self):
        if len(self.left) - len(self.right) == 2:
            self.right.push(self.left.pop())
        elif len(self.left) - len(self.right) == -2:
            self.left.push(self.right.pop())

    def addNum(self, num):
        if len(self.left) == 0:
            self.left.push(num)
            return
        if num <= self.left[0]:
            self.left.push(num)
        else:
            self.right.push(num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] + self.left[0]) / 2.0
        return float(self.left[0]) if len(self.left) > len(self.right) else float(self.right[0])

class case(unittest.TestCase):
    def test_1(self):
        m = MedianFinder()
        m.addNum(1)
        m.addNum(2)
        self.assertEqual(1.5, m.findMedian())
        m.addNum(3)
        self.assertEqual(2.0,m.findMedian())
    def test_2(self):
        m = MedianFinder()
        m.addNum(40)
        self.assertEqual(40.00, m.findMedian())
        m.addNum(12)
        self.assertEqual(26.00,m.findMedian())
        m.addNum(16)
        self.assertEqual(16.00,m.findMedian())
