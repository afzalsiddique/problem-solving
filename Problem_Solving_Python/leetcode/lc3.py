from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # template -> https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        freq=Counter()
        repeatingChars=0 # total number of repeating chars
        res=0
        l,r=0,0
        while r<n:
            freq[s[r]]+=1
            if freq[s[r]]>1:
                repeatingChars+=1
            r+=1
            while repeatingChars>0:
                if freq[s[l]]>1:
                    repeatingChars-=1
                freq[s[l]]-=1
                l+=1
            res=max(res,r-l)
        return res
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        sett=set()
        res=0
        l,r=0,0
        while r<n:
            if s[r] not in sett:
                sett.add(s[r])
                r+=1
            else:
                sett.remove(s[l])
                l+=1
            res=max(res,r-l)
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s)->int:
        start = maxLength = 0
        usedChar = {} # (key,value) = (char, index)

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # In the example, "abcdefb" when right pointer is at 2nd 'b',
                # the left pointer will move to 'c'
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength




class MyTestClass(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().lengthOfLongestSubstring('abcabcbb'))
    def test02(self):
        self.assertEqual(1, get_sol().lengthOfLongestSubstring('bbbbbbb'))
    def test03(self):
        self.assertEqual(3, get_sol().lengthOfLongestSubstring('pwwkew'))
    def test04(self):
        self.assertEqual(0, get_sol().lengthOfLongestSubstring(''))
    def test05(self):
        self.assertEqual(1, get_sol().lengthOfLongestSubstring('b'))
    def test06(self):
        self.assertEqual(3, get_sol().lengthOfLongestSubstring('abc'))
    def test07(self):
        self.assertEqual(3, get_sol().lengthOfLongestSubstring('abcabc'))
    def test08(self):
        self.assertEqual(1, get_sol().lengthOfLongestSubstring(' '))
    def test09(self):
        self.assertEqual(6, get_sol().lengthOfLongestSubstring("bbtablud"))
    def test10(self):
        self.assertEqual(2, get_sol().lengthOfLongestSubstring("aab"))
