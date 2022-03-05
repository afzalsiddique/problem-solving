from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # one pass
    # https://www.youtube.com/watch?v=pHm7VOMzJpI
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        count,A,B=[0]*10,0,0
        for i in range(n):
            s,g=int(secret[i]),int(guess[i])
            if s==g:
                A+=1
            else:
                if count[s]<0:
                    B+=1
                if count[g]>0:
                    B+=1
                count[s]+=1
                count[g]-=1
        return str(A)+'A'+str(B)+'B'

class Solution2:
    # very easy. two passes
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        s_di,g_di,A=defaultdict(int),defaultdict(int),0
        for i in range(n):
            if secret[i]==guess[i]:
                A+=1
            else:
                s_di[secret[i]]+=1
                g_di[guess[i]]+=1
        B=0
        for char in set(secret):
            B+=min(s_di[char],g_di[char])
        return str(A)+'A'+str(B)+'B'


class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual("1A3B",get_sol().getHint("1807","7810"))
    def test02(self):
        self.assertEqual("1A1B",get_sol().getHint("1123","0111"))
    def test03(self):
        self.assertEqual("0A0B",get_sol().getHint("1","0"))
    def test04(self):
        self.assertEqual("1A0B",get_sol().getHint("1","1"))
    def test05(self):
        self.assertEqual("0A4B",get_sol().getHint("1122","2211"))
    def test06(self):
        self.assertEqual("0A1B",get_sol().getHint("8493", "7618"))

