import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/rank-teams-by-votes/discuss/524853/Java-O(26n%2B(262-*-log26))-Sort-by-high-rank-vote-to-low-rank-vote
    def rankTeams(self, votes: List[str]) -> str:
        l=len(votes[0])
        def get_arr(): return [0 for _ in range(l+1)]
        mp=defaultdict(get_arr)
        for vote in votes:
            for i in range(l):
                c=vote[i]
                mp[c][i]+=1
        # print(mp)
        for ch in mp:
            mp[ch][-1]= ord(ch)*(-1) # for sorting alphabetically
        # print(mp)
        li=list(set(votes[0]))
        li.sort(key=lambda x: mp[x])
        # print(li)
        return ''.join(li[::-1])


class tester(unittest.TestCase):
    def test_1(self):
        votes = ["ABC","ACB","ABC","ACB","ACB"]
        Output= "ACB"
        self.assertEqual(Output,get_sol().rankTeams(votes))
    def test_2(self):
        votes = ["WXYZ","XYZW"]
        Output= "XWYZ"
        self.assertEqual(Output,get_sol().rankTeams(votes))
    def test_3(self):
        votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
        Output= "ZMNAGUEDSJYLBOPHRQICWFXTVK"
        self.assertEqual(Output,get_sol().rankTeams(votes))
    def test_4(self):
        votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
        Output= "ABC"
        self.assertEqual(Output,get_sol().rankTeams(votes))
    def test_5(self):
        votes = ["M","M","M","M"]
        Output= "M"
        self.assertEqual(Output,get_sol().rankTeams(votes))
    # def test_6(self):
