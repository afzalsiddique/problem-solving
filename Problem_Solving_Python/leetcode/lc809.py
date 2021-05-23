import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def count(self,word):
        # if word='heeelloooohhh'
        # returns
        # res_char = ['h', 'e', 'l', 'o', 'h']
        # res_cnt =   [1,   3,   2,   4,   3])
        # can't use dictionary because dict does not support duplicate keys
        n=len(word)
        if n==0: return [],[]
        res_char=[]
        res_cnt=[]
        left,right=0,0
        while right<n:
            c=word[left]
            while right+1<n and word[right+1]==c:
                right+=1
            res_char.append(c)
            res_cnt.append(right-left+1)
            left=right+1
            right=right+1
        return res_char,res_cnt
    def possible(self, char_s, cnt_s, char_w, cnt_w):
        if len(char_w)!=len(char_s): return False
        for i in range(len(char_w)):
            if char_w[i]!=char_s[i]:
                return False
            if cnt_s[i]<3 and cnt_w[i]!=cnt_s[i]:
                return False
            if cnt_s[i]>=3 and cnt_w[i]>cnt_s[i]:
                return False
        return True

    def expressiveWords(self, s: str, words: List[str]) -> int:
        char_s,cnt_s=self.count(s)
        ans=0
        for word in words:
            char_w,cnt_w=self.count(word)
            if self.possible(char_s, cnt_s, char_w, cnt_w):
                ans+=1
        return ans


class tester(unittest.TestCase):
    def test01(self):
        s = "heeellooo"
        words = ["hello", "hi", "helo"]
        Output= 1
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test02(self):
        s = ""
        words = ["hello", "hi", "helo"]
        Output= 0
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test03(self):
        s = "heeellooo"
        words = ["", "hi", "helo"]
        Output= 0
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test04(self):
        s = "heeellooo"
        words = ["", "", ""]
        Output= 0
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test05(self):
        s = ""
        words = ["", "", ""]
        Output= 3
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test06(self):
        s = "aaa"
        words = ["aaaa"]
        Output= 0
        self.assertEqual(Output, get_sol().expressiveWords(s,words))
    def test07(self):
        s = "dddiiiinnssssssoooo"
        words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
        Output= 3
        self.assertEqual(Output, get_sol().expressiveWords(s,words))

