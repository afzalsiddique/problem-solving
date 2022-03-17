from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left,right,path):
            nonlocal res
            if left==n and right==n:
                res.append(''.join(path))
                return
            if left>n: return
            backtrack(left+1,right,path+['('])
            if left>right:
                backtrack(left,right+1,path+[')'])

        res=[]
        backtrack(0,0,[])
        return res
class Solution2:
    # https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/10980
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(li, my_str, no_of_open, no_of_close, n):
            if len(my_str) == 2 * n:
                li.append(my_str)

            if no_of_open < n:
                generate(li, my_str+"(", no_of_open+1, no_of_close, n)

            if no_of_close < no_of_open:
                generate(li, my_str + ")", no_of_open, no_of_close+1, n)

        li = []
        generate(li, "", 0, 0, n)
        return li
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(["((()))","(()())","(())()","()(())","()()()"],get_sol().generateParenthesis(3))
    def test02(self):
        self.assertEqual(["()"],get_sol().generateParenthesis(1))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
