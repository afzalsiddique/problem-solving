import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findSubstring(self, s:str, words:List[str])->List[int]:
        wordBag = Counter(words)   # count the freq of each word
        wordLen  = len(words[0])
        numWords = len(words)
        totalLen  = wordLen*numWords
        res=[]
        for i in range(len(s)-totalLen+1):   # scan through s
            # For each i, determine if s[i:i+totalLen] is valid
            seen = defaultdict(int)   # reset for each i
            for j in range(i, i+totalLen, wordLen):
                currWord = s[j:j+wordLen]
                if currWord in wordBag:
                    seen[currWord] += 1
                    if seen[currWord] > wordBag[currWord]: break # optimization
                else:   # if not in wordBag
                    break
            if seen == wordBag:
                res.append(i)   # store result
        return res

class tester(unittest.TestCase):
    def test01(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        Output= [0,9]
        self.assertEqual(Output,get_sol().findSubstring(s, words))
    def test02(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        Output= []
        self.assertEqual(Output,get_sol().findSubstring(s, words))
    def test03(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        Output= [6,9,12]
        self.assertEqual(Output,get_sol().findSubstring(s, words))
    def test04(self):
        s = "barfoofoofoothefoobarman"
        words = ["foo","bar"]
        Output= [0,15]
        self.assertEqual(Output,get_sol().findSubstring(s, words))
