from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minimumDistance(self, word: str) -> int:
        def getCord(i): return [i//6,i%6]
        def dist(i,j):
            x1,y1=getCord(i)
            x2,y2=getCord(j)
            return abs(x1-x2)+abs(y1-y2)
        def dp(i,j,word_i):
            if word_i==len(word):
                return 0
            minn=float('inf')
            minn=min(minn,dist(i,j)+)


        word=list(map(lambda x:ord(x)-ord('A'),word))
        pq=[]
        for i in range(26):
            for j in range(i+1,26):
                heappush(pq,[0,i,j,0]) # cost,finger1,finger2,word_idx


        while pq:
            cost,i,j,word_idx=heappop(pq)
            if word_idx==len(word):
                return cost
            k=word[word_idx]
            heappush(pq,[cost+dist(i,k),k,j,word_idx+1]) # use left finger
            heappush(pq,[cost+dist(j,k),i,k,word_idx+1]) # use left finger



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minimumDistance(word = "CAKE"))
    def test2(self):
        self.assertEqual(6, get_sol().minimumDistance(word = "HAPPY"))
    def test3(self):
        self.assertEqual(3, get_sol().minimumDistance(word = "NEW"))
    def test4(self):
        self.assertEqual(7, get_sol().minimumDistance(word = "YEAR"))
    def test5(self):
        self.assertEqual(500, get_sol().minimumDistance(word = "KXGJRDQYJCDRTJXBHDVFOFFOIWFOWSARMADDJCUYMGIXMHOUTQRLFNUZASNTHJLQKPUYXOXWILIYFFHOKUALPTZWJVHADOXQFGMWTKREBPNOZOLAGSGCPEVCXQWVRMTIGCNARPWXKXAGTJYYZNOWQWJCBCLMUNMZUWYUYHJPMRAUNUJVPEMVNMWYSXTJPRLJNSUYFLBNOOJCVHKHMATKEFPCYDFTBHUFAUQVNVNFJMOJRBFPFDVDPXJXZJJMBSIK"))
