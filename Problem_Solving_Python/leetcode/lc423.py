import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/1131046/Python-Linear-solution-using-Counters-explained
    def originalDigits(self, s):
        cnt = Counter(s)
        Digits = ["zero","two","four","six","eight","one","three","five","seven","nine"]
        Corresp = [0,2,4,6,8,1,3,5,7,9]
        Counters = [Counter(digit) for digit in Digits]
        Found = [0]*10
        for it, C in enumerate(Counters):
            k = min(cnt[x]//C[x] for x in C)
            for i in C.keys(): C[i] *= k
            cnt -= C
            Found[Corresp[it]] = k

        return "".join([str(i)*Found[i] for i in range(10)])
class Solution2:
    # tle
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        di = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
        def take_out(digit,counter):
            digit_in_word = di[digit]
            for c in digit_in_word:
                counter[c]-=1
        def put_back(digit,counter):
            digit_in_word = di[digit]
            for c in digit_in_word:
                counter[c]+=1
        def is_exhausted(counter):
            for c in counter:
                if counter[c]<0: return True
            return False
        def is_empty(counter):
            for c in counter:
                if counter[c]!=0: return False
            return True

        def helper():
            if is_exhausted(counter): return False
            if is_empty(counter): return True
            for i in range(0,9+1):
                path.append(i)
                take_out(i,counter)
                if helper(): return True
                put_back(i,counter)
                path.pop()

        path=[]
        helper()
        return ''.join(list(map(str,path)))

class tester(unittest.TestCase):
    def test01(self):
        s = "owoztneoer"
        Output= "012"
        self.assertEqual(Output,get_sol().originalDigits(s))
    def test02(self):
        s = "fviefuro"
        Output= "45"
        self.assertEqual(Output,get_sol().originalDigits(s))
    def test03(self):
        s = "zeroonetwothreefourfivesixseveneightnine"
        Output= "0123456789"
        self.assertEqual(Output,get_sol().originalDigits(s))
