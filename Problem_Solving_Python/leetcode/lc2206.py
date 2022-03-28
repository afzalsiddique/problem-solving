from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n=len(text)
        pre=[0]*n
        prev=0
        for i in range(n):
            if text[i]==pattern[0]:
                pre[i]=prev+1
            else:
                pre[i]=prev
            prev=pre[i]

        suf=[0]*n
        prev=0
        for i in range(n-1,-1,-1):
            if text[i]==pattern[1]:
                suf[i]=prev+1
            else:
                suf[i]=prev
            prev=suf[i]

        res=0
        for i in range(n-1):
            if text[i]==pattern[0]:
                res+=suf[i+1]
        option2=suf[0]
        option1=pre[-1]

        return res+max(option1,option2)




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().maximumSubsequenceCount("abdcdbc", "ac"))
    def test02(self):
        self.assertEqual(6,get_sol().maximumSubsequenceCount("aabb", "ab"))
    def test03(self):
        self.assertEqual(1,get_sol().maximumSubsequenceCount("a", "ac"))
