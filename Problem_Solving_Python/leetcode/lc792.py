import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # binary search
    # time O(len(S)+O(numbers of letters in all words)*log(occurrence of the letter occurring the most))
    # https://leetcode.com/problems/number-of-matching-subsequences/discuss/117578/Simple-Python-solution
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            di_i = 0
            for c in word:
                li=di[c]
                if len(li)==0 or di_i>li[-1]: return False
                tmp = bisect_left(li,di_i)
                idx = li[tmp]
                if idx<di_i: return False
                di_i=idx+1
            return True

        di = defaultdict(list)
        for i,c in enumerate(s):
            di[c].append(i)

        cnt=0
        for word in words:
            if is_subsequence(word): cnt+=1
        return cnt

class Solution2:
    # tle
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            if len(word)>len(s): return False
            i,j=0,0
            while i<len(s) and j<len(word):
                if s[i]==word[j]:
                    j+=1
                i+=1
            if j==len(word): return True
            return False

        cnt=0
        for word in words:
            if is_subsequence(word):
                cnt+=1
        return cnt
class tester(unittest.TestCase):
    def test1(self):
        s = "abcde"
        words = ["a","bb","acd","ace"]
        Output= 3
        self.assertEqual(Output,Solution().numMatchingSubseq(s,words))
    def test2(self):
        s = "dsahjpjauf"
        words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        Output= 2
        self.assertEqual(Output,Solution().numMatchingSubseq(s,words))
    def test3(self):
        s = "aacbacbde"
        words = ["abcb"]
        Output= 1
        self.assertEqual(Output,Solution().numMatchingSubseq(s,words))
