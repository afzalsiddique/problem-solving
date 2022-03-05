from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i,path):
            if i==n:
                res.append(''.join(path))
                return
            for c in di[digits[i]]:
                dfs(i+1,path+[c])

        n=len(digits)
        if n==0: return []
        di={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        dfs(0,[])
        return res
class Solution2:
    # https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/10980
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        def helper(li, mystr, digits):
            i = len(mystr)
            if len(mystr) == len(digits):
                li.append(mystr)
                return

            if digits[i] == '2':
                helper(li, mystr + "a", digits)
                helper(li, mystr + "b", digits)
                helper(li, mystr + "c", digits)

            if digits[i] == '3':
                helper(li, mystr + "d", digits)
                helper(li, mystr + "e", digits)
                helper(li, mystr + "f", digits)

            if digits[i] == '4':
                helper(li, mystr + "g", digits)
                helper(li, mystr + "h", digits)
                helper(li, mystr + "i", digits)

            if digits[i] == '5':
                helper(li, mystr + "j", digits)
                helper(li, mystr + "k", digits)
                helper(li, mystr + "l", digits)

            if digits[i] == '6':
                helper(li, mystr + "m", digits)
                helper(li, mystr + "n", digits)
                helper(li, mystr + "o", digits)

            if digits[i] == '7':
                helper(li, mystr + "p", digits)
                helper(li, mystr + "q", digits)
                helper(li, mystr + "r", digits)
                helper(li, mystr + "s", digits)

            if digits[i] == '8':
                helper(li, mystr + "t", digits)
                helper(li, mystr + "u", digits)
                helper(li, mystr + "v", digits)

            if digits[i] == '9':
                helper(li, mystr + "w", digits)
                helper(li, mystr + "x", digits)
                helper(li, mystr + "y", digits)
                helper(li, mystr + "z", digits)

        li = []
        helper(li, "", digits)
        return li
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(["ad","ae","af","bd","be","bf","cd","ce","cf"],get_sol().letterCombinations("23"))
    def test02(self):
        self.assertEqual([],get_sol().letterCombinations(""))
    def test03(self):
        self.assertEqual(["a","b","c"],get_sol().letterCombinations("2"))
