import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/word-subsets/discuss/1128187/Python-Simple-counter-solution-explained
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        di=defaultdict(int)
        for b in words2:
            counter = Counter(b)
            for ch in counter:
                di[ch]=max(di[ch],counter[ch])

        # print(di)
        res=[]
        for a in words1:
            flag=True
            counter = Counter(a)
            for ch in di:
                if counter[ch]<di[ch]:
                    flag=False
            if flag:
                res.append(a)
        return res
class Solution2:
    # tle
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def check(di1:Counter,di2:Counter):
            for ch in di2:
                if di1[ch]<di2[ch]: return False
            return True

        arr1 = [Counter(words1[i]) for i in range(len(words1))]
        arr2 = [Counter(words2[i]) for i in range(len(words2))]
        res = []
        for i in range(len(words1)):
            flag=True
            for j in range(len(words2)):
                if not check(arr1[i],arr2[j]):
                    flag=False
                    break
            if flag: res.append(words1[i])
        return res


class tester(unittest.TestCase):
    def test01(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["e","o"]
        Output= ["facebook","google","leetcode"]
        self.assertEqual(Output,get_sol().wordSubsets(words1,words2))
    def test02(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["l","e"]
        Output= ["apple","google","leetcode"]
        self.assertEqual(Output,get_sol().wordSubsets(words1,words2))
    def test03(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["e","oo"]
        Output= ["facebook","google"]
        self.assertEqual(Output,get_sol().wordSubsets(words1,words2))
    def test04(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["lo","eo"]
        Output= ["google","leetcode"]
        self.assertEqual(Output,get_sol().wordSubsets(words1,words2))
    def test05(self):
        words1 = ["amazon","apple","facebook","google","leetcode"]
        words2 = ["ec","oc","ceo"]
        Output= ["facebook","leetcode"]
        self.assertEqual(Output,get_sol().wordSubsets(words1,words2))
