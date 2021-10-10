import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(n): return SeatManager(n)
class SeatManager:
    def __init__(self, n: int):
        self.hp = [x for x in range(1,n+1)]
        heapify(self.hp)
    def reserve(self) -> int:
        return heappop(self.hp)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.hp,seatNumber)


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='SeatManager':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='reserve':
                outputs.append(obj.reserve())
            elif cmd=='unreserve':
                outputs.append(obj.unreserve(input[0]))
        return outputs
    def test_01(self):
        commands = ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
        inputs=[[5], [], [], [2], [], [], [], [], [5]]
        expected = [None, 1, 2, None, 2, 3, 4, 5, None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
