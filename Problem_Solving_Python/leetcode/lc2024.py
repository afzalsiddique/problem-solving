import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# same as leetcode 424
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        left,right = 0,0
        count = Counter()
        count['#']=0
        res = 0
        while right<n:
            count[answerKey[right]]+=1
            right+=1
            while right-left-max(count.values())>k:
                count[answerKey[left]]-=1
                left+=1
            res=max(res,right-left)
        return res
class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        left,right = 0,0
        count = Counter()
        count['#']=0
        res = 0
        while right<n:
            if right-left-max(count.values())>k:
                count[answerKey[left]]-=1
                left+=1
            while right<n and right-left-max(count.values())<=k:
                count[answerKey[right]]+=1
                right+=1
                if right-left-max(count.values())<=k:
                    res=max(res,right-left)
        return res
class Solution3:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(letter):
            n=len(answerKey)
            left,right = 0,0
            cnt = 0
            res = 0
            while right<n:
                if cnt>k:
                    cnt-= answerKey[left] == letter
                    left+=1
                while right<n and cnt<=k:
                    cnt+= answerKey[right] == letter
                    right+=1
                    if cnt<=k:
                        res=max(res,right-left)
            return res
        return max(f('F'),f('T'))
class Solution4:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(letter):
            n=len(answerKey)
            left,right = 0,0
            cnt = 0
            res = 0
            while right<n:
                if cnt<=k:
                    cnt+= answerKey[right] == letter
                    right+=1
                else:
                    cnt-= answerKey[left] == letter
                    left+=1
                if cnt<=k:
                    res=max(res,right-left)
            return res
        return max(f('F'),f('T'))
class MyTestCase(unittest.TestCase):
    def test1(self):
        answerKey,k = "TTFF",  2
        Output= 4
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
    def test2(self):
        answerKey,k = "TFFT",  1
        Output= 3
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
    def test3(self):
        answerKey,k = "TTFTTFTT",  1
        Output= 5
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
    def test4(self):
        answerKey,k = "F", 1
        Output= 1
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
    def test5(self):
        answerKey,k = "TF", 2
        Output= 2
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
    def test6(self):
        answerKey,k = "FTFFTFTFTTFTTFTTFFTTFFTTTTTFTTTFTFFTTFFFFFTTTTFTTTTTTTTTFTTFFTTFTFFTTTFFFFFTTTFFTTTTFTFTFFTTFTTTTTTF", 32
        Output= 85
        self.assertEqual(Output, get_sol().maxConsecutiveAnswers(answerKey,k))
