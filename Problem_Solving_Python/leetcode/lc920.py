from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=gk4qzZSmyrs
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        M=10**9+7
        @cache
        def count(cur_goal,old_songs):
            if cur_goal==0 and old_songs==n:
                return 1
            if cur_goal==0 or old_songs>n:
                return 0
            # new songs
            res=(n-old_songs)*count(cur_goal-1,old_songs+1)
            if old_songs>k:
                # old songs
                res+=(old_songs-k)*count(cur_goal-1,old_songs)
            return res%M

        return count(goal,0)



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(6,get_sol().numMusicPlaylists(3, 3, 1))
    def test02(self):
        self.assertEqual(6,get_sol().numMusicPlaylists(2,3,0))
    def test03(self):
        self.assertEqual(2,get_sol().numMusicPlaylists(2,3,1))
    def test04(self):
        self.assertEqual(2,get_sol().numMusicPlaylists(100,100,100))
    def test05(self):
        self.assertEqual(2,get_sol().numMusicPlaylists(100,100,0))
    def test06(self):
        self.assertEqual(2,get_sol().numMusicPlaylists(100,50,50))
