import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


# one pass
# https://www.youtube.com/watch?v=pHm7VOMzJpI
class Solution:
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

# very easy. two passes
class Solution2:
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
    def test1(self):
        secret = "1807"
        guess = "7810"
        Output= "1A3B"
        self.assertEqual(Output,Solution().getHint(secret,guess))
    def test2(self):
        secret = "1123"
        guess = "0111"
        Output= "1A1B"
        self.assertEqual(Output,Solution().getHint(secret,guess))
    def test3(self):
        secret = "1"
        guess = "0"
        Output= "0A0B"
        self.assertEqual(Output,Solution().getHint(secret,guess))
    def test4(self):
        secret = "1"
        guess = "1"
        Output= "1A0B"
        self.assertEqual(Output,Solution().getHint(secret,guess))
    def test5(self):
        secret = "1122"
        guess = "2211"
        Output= "0A4B"
        self.assertEqual(Output,Solution().getHint(secret,guess))
