from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        M=10**9+7
        @cache
        def unique_letters(i,j):
            return len(set(s[i:j+1]))
        @cache
        def dp(i,j,prev_equal):
            if i>j: return 0
            ans=0
            if s[i]==s[j]:
                if prev_equal:
                    ans+=unique_letters(i,j)
                ans+=dp(i+1,j-1,True)
            else:
                ans+=dp(i+1,j,False)
                ans+=dp(i,j-1,False)
            ans%=M
            return ans

        return dp(0,len(s)-1,True)

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6,get_sol().countPalindromicSubsequences('bccb'))
    def test_2(self):
        self.assertEqual(104860361,get_sol().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
