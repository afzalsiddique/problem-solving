import unittest
from collections import defaultdict
from heapq import *
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq=[]
        for pas,total in classes:
            before = pas/total
            after = (pas+1)/(total+1)
            improve = after-before
            pq.append((-improve,pas+1,total+1))
        heapify(pq)

        while extraStudents:
            improve, pas, total = heappop(pq)
            before = pas/total
            after = (pas+1)/(total+1)
            new_improve = after-before
            heappush(pq, (-new_improve, pas+1, total+1))
            extraStudents-=1

        avg = 0
        while pq:
            improve, pas, total = heappop(pq)
            avg += (pas-1)/(total-1)
        avg = avg / len(classes)
        return avg



class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual =Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], extraStudents = 4)
        expected = 0.53485
        self.assertEqual(expected, actual)
    def test_2(self):
        actual =Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
        expected = 0.78333
        self.assertEqual(expected, actual)
