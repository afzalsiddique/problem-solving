from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # kmp
    # https://www.youtube.com/watch?v=c4akpqTwE5g
    # time O(n) space O(n)
    def shortestPalindrome(self, s: str) -> str:
        def get_lps(pat:str):
            n = len(pat)
            lps = [0]*n
            i=1
            j=0
            while i<n:
                if pat[i]==pat[j]:
                    lps[i]=j+1
                    i+=1
                    j+=1
                else:
                    if j==0:
                        i+=1
                    else:
                        j=lps[j-1]
            return lps

        if s==s[::-1]: return s
        rev_s = s[::-1]
        new_s = s+'#'+rev_s
        lps = get_lps(new_s)
        cut = lps[-1]
        temp = rev_s[:len(rev_s)-cut]
        return temp+s

    # brute force
    # time O(n^2)
    # space O(n). because new_s is a string whose memory is O(n)
    def shortestPalindrome2(self, s: str) -> str:
        if not s: return s
        if s==s[::-1]: return s
        n=len(s)
        for i in reversed(range(n)):
            pre=s[i:]
            new_s=pre[::-1]+s
            if new_s==new_s[::-1]: return new_s

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("aaacecaaa",get_sol().shortestPalindrome("aacecaaa"))
    def test2(self):
        self.assertEqual("dcbabcd",get_sol().shortestPalindrome("abcd"))
    def test3(self):
        self.assertEqual("a",get_sol().shortestPalindrome("a"))
    def test4(self):
        self.assertEqual("",get_sol().shortestPalindrome(""))
    def test5(self):
        self.assertEqual("abbaabba",get_sol().shortestPalindrome("aabba"))
