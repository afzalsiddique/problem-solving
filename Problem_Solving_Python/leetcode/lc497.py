import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return Solution2(x)
# THE INPUT MAY CONTAIN LINES THAT ARE NOT RECTANGLES. FOR EXAMPLE, [1, 2, 1, 5], [3, 2, 3, -2]

# class Solution:
    # use binary search with cumulative sum
class Solution2:
    # weighted probability
    def __init__(self, rects: List[List[int]]):
        def prob(a,b,x,y):
            dx = x-a + 1 # +1 because perimeter also included
            dy = y-b + 1
            return dx*dy
        self.rects = rects
        self.li = [i for i in range(len(rects))]
        self.area = [prob(a,b,x,y)  for a, b, x, y in rects]
    def pick(self) -> List[int]:
        rec_id = random.choices(self.li, self.area)[0]
        a,b,x,y = self.rects[rec_id]
        return [random.randint(a,x), random.randint(b,y)]

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Solution':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='pick':
                outputs.append(obj.pick())
        return outputs
    def test_01(self):
        commands = ["Solution", "pick", "pick", "pick", "pick", "pick"]
        inputs=[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
        expected = [None, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
