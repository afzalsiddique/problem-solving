import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

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

class tester(unittest.TestCase):
    def test1(self):
        s = "aacecaaa"
        Output= "aaacecaaa"
        self.assertEqual(Output,Solution().shortestPalindrome(s))
    def test2(self):
        s = "abcd"
        Output= "dcbabcd"
        self.assertEqual(Output,Solution().shortestPalindrome(s))
    def test3(self):
        s = "a"
        Output= "a"
        self.assertEqual(Output,Solution().shortestPalindrome(s))
    def test4(self):
        s = ""
        Output= ""
        self.assertEqual(Output,Solution().shortestPalindrome(s))
    def test5(self):
        s = "aabba"
        Output= "abbaabba"
        self.assertEqual(Output,Solution().shortestPalindrome(s))
