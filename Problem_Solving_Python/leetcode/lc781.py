import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/rabbits-in-forest/discuss/114715/Java-Solution-with-HashMap-O(N)-and-comments
    def numRabbits(self, answers: List[int]) -> int:
        n=len(answers)
        if not n: return 0
        di={}
        summ=0
        for ans in answers:
            if ans==0: # unique rabbit
                summ+=1
                continue
            if ans not in di: # first time with this color
                di[ans]=0
                summ+=ans+1 # other rabbits + 1(the rabbit we are talking to)
            else:
                di[ans]+=1
                # if there are k of each color then they are all present, remove them to allow the change to account for others.
                if di[ans]==ans:
                    di.pop(ans)
        return summ

class tester(unittest.TestCase):
    def test_1(self):
        answers,Output = [2,2,2,3], 7
        self.assertEqual(Output, get_sol().numRabbits(answers))
    def test_2(self):
        answers,Output = [1,1,2], 5
        self.assertEqual(Output, get_sol().numRabbits(answers))
    def test_3(self):
        answers,Output = [10,10,10], 11
        self.assertEqual(Output, get_sol().numRabbits(answers))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):