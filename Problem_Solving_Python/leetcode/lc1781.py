import heapq
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        summ=0
        for left in range(n):
            freq = [0]*26
            for right in range(left,n):
                freq[ord(s[right])-97]+=1
                summ += max(freq) - min(x for x in freq if x!=0)
        return summ
class Solution2:
    # not good
    def beautySum(self, s: str) -> int:
        def get_beauty(mystr:str):
            count = Counter(mystr)
            maxx=max(count.values())
            minn=min(count.values())
            return maxx-minn

        n=len(s)
        summ=0
        for left in range(n):
            for right in range(left+1,n+1):
                summ+=get_beauty(s[left:right])
        return summ

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "aabcb"
        Output= 5
        self.assertEqual(Output, get_sol().beautySum(s))
    def test_2(self):
        s = "aabcbaa"
        Output= 17
        self.assertEqual(Output, get_sol().beautySum(s))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):