import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        ALICEWINS,BOBWINS,DRAW=1,-1,0
        n=len(aliceValues)
        li = []
        for i,(a,b) in enumerate(zip(aliceValues,bobValues)):
            li.append( ( (a+b)*(-1), i)  ) # multiply by -1 because it is a max_heap
        li.sort(reverse=True)
        aliceTurn=True
        alicePoints,bobPoints = 0,0
        while li:
            _,idx = li.pop()
            if aliceTurn:
                alicePoints += aliceValues[idx]
            else:
                bobPoints += bobValues[idx]
            aliceTurn = not aliceTurn
        return ALICEWINS if alicePoints>bobPoints else BOBWINS if bobPoints>alicePoints else DRAW
class Solution2:
    # wrong ans
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        ALICEWINS,BOBWINS,DRAW=1,-1,0
        mn_hp = [(abs(a-b),i) for i,(a,b) in enumerate(zip(aliceValues,bobValues))]
        mx_hp = [(abs(a-b)*(-1),i) for i,(a,b) in enumerate(zip(aliceValues,bobValues))]
        heapify(mx_hp)
        heapify(mn_hp)
        aliceTurn=True
        alicePoints,bobPoints = 0,0
        while mx_hp:
            _,idx = heappop(mx_hp)
            heappop(mn_hp)
            if aliceTurn:
                alicePoints+=aliceValues[idx]
            else:
                bobPoints+=bobValues[idx]
            # if aliceTurn:
            #     print('alice:',alicePoints)
            # else:
            #     print('bob:',bobPoints)
            aliceTurn=not aliceTurn

        if alicePoints>bobPoints:
            return ALICEWINS
        elif bobPoints>alicePoints:
            return BOBWINS
        return DRAW


class MyTestCase(unittest.TestCase):
    def test1(self):
        aliceValues,bobValues = [1,3],  [2,1]
        Output= 1
        self.assertEqual(Output, get_sol().stoneGameVI(aliceValues,bobValues))
    def test2(self):
        aliceValues,bobValues = [1,2],  [3,1]
        Output= 0
        self.assertEqual(Output, get_sol().stoneGameVI(aliceValues,bobValues))
    def test3(self):
        aliceValues,bobValues = [2,4,3],  [1,6,7]
        Output= -1
        self.assertEqual(Output, get_sol().stoneGameVI(aliceValues,bobValues))
    def test4(self):
        aliceValues,bobValues = [9,8,3,8], [10,6,9,5]
        Output= 1
        self.assertEqual(Output, get_sol().stoneGameVI(aliceValues,bobValues))
