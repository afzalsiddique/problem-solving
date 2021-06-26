import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def canMeasureWater(self, x, y, z)->bool:
        if z > x + y:
            return False

        # set the initial state will empty jars;
        q = deque()
        q.append((0,0))
        visited = {(0,0)}
        while len(q) > 0:
            a, b = q.popleft()
            if a + b == z:
                return True

            states = set()

            states.add((x, b)) # fill jar x;
            states.add((a, y)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;

            # pour from y to x
            if a+b<x:
                states.add((min(x,a+b),0))
            else:
                states.add((min(x,a+b),b-(x-a)))
            # pour from x to y
            if a+b<y:
                states.add((0,min(a+b, y)))
            else:
                states.add((a-(y-b),min(a+b, y)))

            for state in states:
                if state in visited:
                    continue
                q.append(state)
                visited.add(state)

        return False



class tester(unittest.TestCase):
    def test_01(self):
        jug1Capacity = 3
        jug2Capacity = 5
        targetCapacity = 4
        Output= True
        self.assertEqual(Output, get_sol().canMeasureWater(jug1Capacity,jug2Capacity,targetCapacity) )
    def test_02(self):
        jug1Capacity = 2
        jug2Capacity = 6
        targetCapacity = 5
        Output= False
        self.assertEqual(Output, get_sol().canMeasureWater(jug1Capacity,jug2Capacity,targetCapacity) )
    def test_03(self):
        jug1Capacity = 1
        jug2Capacity = 2
        targetCapacity = 3
        Output= True
        self.assertEqual(Output, get_sol().canMeasureWater(jug1Capacity,jug2Capacity,targetCapacity) )
