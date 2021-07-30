import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    # If you don't find the winner after one pass,
    # the winner will be max(A),
    # bacause no one will beats him anymore.
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        count=Counter()
        for _ in range(len(arr)):
            if q[1]>q[0]:
                count[q[1]]+=1
                q.append(q.popleft())
            else:
                count[q[0]]+=1
                first=q.popleft()
                q.append(q.popleft())
                q.appendleft(first)
            if count[q[0]]==k: return q[0]
        return max(arr)


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [2,1,3,5,4,6,7]
        k = 2
        Output= 5
        self.assertEqual(Output,get_sol().getWinner(arr,k))
    def test2(self):
        arr = [3,2,1]
        k = 10
        Output= 3
        self.assertEqual(Output,get_sol().getWinner(arr,k))
    def test3(self):
        arr = [1,9,8,2,3,7,6,4,5]
        k = 7
        Output= 9
        self.assertEqual(Output,get_sol().getWinner(arr,k))
    def test4(self):
        arr = [1,11,22,33,44,55,66,77,88,99]
        k = 1000000000
        Output= 99
        self.assertEqual(Output,get_sol().getWinner(arr,k))
    def test5(self):
        arr = [22,1,44,11,33,55,66,77,88,99]
        k = 1000000000
        Output= 99
        self.assertEqual(Output,get_sol().getWinner(arr,k))
