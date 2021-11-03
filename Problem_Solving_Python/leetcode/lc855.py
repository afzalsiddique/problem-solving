import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return ExamRoom(x)
class ExamRoom:
    # wrong
    def __init__(self, n: int):
        self.pq = []
        heappush(self.pq,(float('-inf'),0,n-1))
        heappush(self.pq,(float('-inf'),n-1,0))
        self.occupied = [False]*n
    def seat(self) -> int:
        pq = self.pq
        while True:
            diff, left,right = heappop(pq)
            diff*=-1
            if diff==float('inf'):
                res = left
            else:
                res = (left+right)//2
            if not self.occupied[res]:
                self.occupied[res]=True
                heappush(pq, (-(res-1-left),left,right-1))
                heappush(pq, (-right-(left+1),left+1,right))
                break
        return res
    def leave(self, p: int) -> None:
        self.occupied[p]=False

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='ExamRoom':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='seat':
                outputs.append(obj.seat())
            elif cmd=='leave':
                outputs.append(obj.leave(input[0]))
        return outputs
    def test_01(self):
        commands = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
        inputs=[[10], [], [], [], [], [4], []]
        expected = [None, 0, 9, 4, 2, None, 5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
