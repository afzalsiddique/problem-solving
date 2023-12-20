import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = Counter(s)
        freq_count=defaultdict(int) # 'aaabbbcc' -> {3:2,2:1} There are 2 chars with 3 frequency and 1 char with 2 frequency
        for ch in char_count:
            freq_count[char_count[ch]]+=1
        res=0
        maxx=max(freq_count)
        for i in range(maxx,0,-1):
            if freq_count[i]>1:
                tmp = freq_count[i]-1
                freq_count[i]=1
                freq_count[i-1] += tmp
                res+=tmp
        return res
class Solution2:
    def minDeletions(self, s: str) -> int:
        ENOUGH = 10**5+5
        count = Counter(s)
        freq=[0 for _ in range(ENOUGH)]
        for ch in count:
            freq[count[ch]]+=1
        res=0
        for i in range(ENOUGH-1,0,-1):
            if freq[i]>1:
                tmp = freq[i]-1
                freq[i]=1
                freq[i-1] += tmp
                res+=tmp
        return res


class tester(unittest.TestCase):
    def test_1(self):
        s = "aab"
        Output= 0
        self.assertEqual(Output, get_sol().minDeletions(s))
    def test_2(self):
        s = "aaabbbcc"
        Output= 2
        self.assertEqual(Output, get_sol().minDeletions(s))
    def test_3(self):
        s = "ceabaacb"
        Output= 2
        self.assertEqual(Output, get_sol().minDeletions(s))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):