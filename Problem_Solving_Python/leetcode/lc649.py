import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # each person will ban other party's first member to his right
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        q1 = deque([i for i in range(n) if senate[i]=='R'])
        q2 = deque([i for i in range(n) if senate[i]=='D'])
        while q1 and q2:
            r_idx=q1.popleft()
            d_idx=q2.popleft()
            if r_idx<d_idx: # if r can ban d
                q1.append((r_idx+n)) # then r will appear r_idx+n th position next time
            else:
                q2.append((d_idx+n))
        return 'Radiant' if len(q1)>len(q2) else 'Dire'
class Solution2:
    # very slow
    def predictPartyVictory(self, senate: str) -> str:
        count=Counter(senate)
        senate=list(senate)
        while True:
            n=len(senate)
            banned = [False for _ in range(n)]
            for i in range(n):
                if not count['D']: return 'Radiant'
                if not count['R']: return 'Dire'
                if banned[i]: continue
                if senate[i]=='D':
                    j=(i+1) %n
                    while j!=i:
                        if senate[j]=='R' and not banned[j]:
                            banned[j]=True
                            break
                        j= (j+1)%n
                    count['R']-=1
                if senate[i]=='R':
                    j=(i+1) %n
                    while j!=i:
                        if senate[j]=='D' and not banned[j]:
                            banned[j]=True
                            break
                        j= (j+1)%n
                    count['D']-=1
            senate=[senate[i] for i in range(n) if not banned[i]] # keep only those who are not banned


class Tester(unittest.TestCase):
    def test_1(self):
        senate = "RD"
        Output= "Radiant"
        self.assertEqual(Output,get_sol().predictPartyVictory(senate))
    def test_2(self):
        senate = "RDD"
        Output= "Dire"
        self.assertEqual(Output,get_sol().predictPartyVictory(senate))
    def test_3(self):
        senate = "RRDDD"
        Output= "Radiant"
        self.assertEqual(Output,get_sol().predictPartyVictory(senate))
    def test_4(self):
        senate = "DRRDRDRDRDDRDRDR"
        Output= "Radiant"
        self.assertEqual(Output,get_sol().predictPartyVictory(senate))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
