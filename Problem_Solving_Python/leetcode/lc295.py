import unittest
from heapq import *


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == 0:
            heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)
        if len(self.small) - len(self.large) == 2:
            heappush(self.large, -heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heappush(self.small, -heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2.0
        return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])


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
