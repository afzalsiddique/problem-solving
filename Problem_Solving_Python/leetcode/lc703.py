import unittest
from heapq import *
from typing import List




class KthLargest:

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

class case(unittest.TestCase):
    def test_1(self):
        k = KthLargest(3, [4,5,8,2])
        self.assertEqual(4,k.add(3))
