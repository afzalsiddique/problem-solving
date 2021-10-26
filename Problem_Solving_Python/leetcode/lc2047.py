import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(word):
            n=len(word)
            li = word.split('-')
            if len(li)>=3: return False
            if len(li)==2:
                left,right = li[0],li[1]
                if ',.!' in left: return False
                cnt = 0
                for i in range(len(right)):
                    if right[i] in 'abcdefghijklmnopqrstuvwxyz':
                        cnt+=1
                if cnt==0: return False

            no_hyphen=0
            no_punc=0
            for i in range(n):
                if '0'<=word[i]<='9': return False
                if word[i]=='-': no_hyphen+=1
                if word[i] in ',.!': no_punc+=1

                if i==n-1:
                    if word[i]=='-': return False
                elif 0<i<n-1:
                    if word[i] in ',.!': return False
                else:
                    if word[i]=='-': return False
                    if word[i] in ',.!': return False
            if no_punc<=1 and no_hyphen<=1: return True
            return False

        li = sentence.split()
        res = 0
        for word in li:
            res+=valid(word)
        return res
class MyTestCase(unittest.TestCase):
    def test1(self):
        sentence = "cat and  dog"
        Output= 3
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test2(self):
        sentence = "!this  1-s b8d!"
        Output= 0
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test3(self):
        sentence = "alice and  bob are playing stone-game10"
        Output= 5
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test4(self):
        sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
        Output= 6
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test5(self):
        sentence = "!"
        Output= 1
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test6(self):
        sentence = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
        Output= 49
        self.assertEqual(Output, get_sol().countValidWords(sentence))
    def test7(self):
        sentence = "b-a-c f-d"
        Output= 1
        self.assertEqual(Output, get_sol().countValidWords(sentence))
