import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# class Solution:
# https://leetcode.com/problems/stickers-to-spell-word/discuss/161470/My-Python-DFS-Solution/333443

class Solution:
    # tle
    def minStickers(self, stickers: List[str], target: str) -> int:
        def func(s): return Counter(c for c in s if c in target)
        def subtract_available(c1,c2):
            for c in c2:
                if c in c1: return True
            return False
        def hash(count:Counter): # hash a Counter
            li = [str(count[c]) for c in string.ascii_lowercase]
            return ','.join(li)
        def unhash(hashed:str): # unhash the Counter
            li = hashed.split(',')
            count = Counter()
            for c in string.ascii_lowercase:
                idx = ord(c)-ord('a')
                if int(li[idx]):
                    count[c]=int(li[idx])
            return count
        @functools.lru_cache(None)
        def backtrack(i,hashed:str):
            count=unhash(hashed)
            if all(count[c]==0 for c in count): return 0
            res=float('inf')
            for j in range(i,n):
                if subtract_available(count,freqs[j]):
                    res=min(res,1+backtrack(j,hash(count-freqs[j])))
            return res


        n=len(stickers)
        freqs=[func(s) for s in stickers]
        res= backtrack(0,hash(Counter(target)))
        return res if res!=float('inf') else -1



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().minStickers(stickers = ["with","example","science"], target = "thehat"))
    def test2(self):
        self.assertEqual(-1,get_sol().minStickers(stickers = ["notice","possible"], target = "basicbasic"))
    def test3(self):
        self.assertEqual(3,get_sol().minStickers(["these","guess","about","garden","him"], "atomher"))
    def test4(self):
        self.assertEqual(3,get_sol().minStickers(["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease"))
    def test5(self):
        self.assertEqual(3,get_sol().minStickers(["point","square","love","show","ran","certain","soil","period","say","human","duck","meet","speed","lie","differ","depend","thank","floor","sail","father","spring","field","music","too","interest","suit","new","finish","electric","parent","song","read","who","effect","fall","spoke","on","short","center","organ","plain","straight","near","so","she","science","quick","position","problem","history"], "chargeresult"))
    # def test6(self):
    # def test7(self):
    # def test8(self):
