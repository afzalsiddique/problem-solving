from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99583/Python-Simple-(Two-pointer)
    # https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/1077674/Python-O(mn)-solution-explained
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x:(-len(x),x))
        for word in d:
            if self.is_substring(s, word):
                return word
        return ""
    def is_substring(self, s, word):
        j=0
        for i in range(len(s)):
            if word[j]==s[i]:
                j+=1
            if j==len(word):
                return True
        return False


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual("apple", get_sol().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
    def test02(self):
        self.assertEqual("a", get_sol().findLongestWord("abpcplea", ["a","b","c"]))

