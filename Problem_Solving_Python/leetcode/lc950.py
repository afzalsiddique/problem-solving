import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # using queue
    # https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/200526/Java-Queue-Simulation-Step-by-Step-Explanation
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        q = deque([i for i in range(n)])
        res = [-1 for _ in range(n)]
        for i in range(n):
            res[q.popleft()] = deck[i]
            if q:
                q.append(q.popleft())
        return res
class Solution2:
    # using deque
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort(reverse=True)
        d = deque()
        for i in range(n):
            d.rotate()
            d.appendleft(deck[i])
        return list(d)
class tester(unittest.TestCase):
    def test1(self):
        Input= [17,13,11,2,3,5,7]
        Output= [2,13,3,11,5,17,7]
        self.assertEqual(Output,get_sol().deckRevealedIncreasing(Input))