from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            # if c=='[': continue # wrong. '2[2[y]]' -> 'yyyyyyyyyyyyyyyyyyyyyy' instead of '2222'
            if c == ']':
                temp = []
                while st[-1]!='[': # pop everything inside []
                    temp.append(st.pop())
                temp.reverse()
                st.pop() # pop '['
                cnt = []
                while st and '0'<=st[-1]<='9': # pop num
                    cnt.append(st.pop())
                cnt.reverse()
                cnt = int("".join(cnt))
                temp = "".join(temp)*cnt
                st.append(temp)
            else:
                st.append(c)
        return "".join(st)
class mycase(unittest.TestCase):
    def test01(self):
        self.assertEqual("aaabcbc",get_sol().decodeString("3[a]2[bc]"))
    def test02(self):
        self.assertEqual("accaccacc",get_sol().decodeString("3[a2[c]]"))
    def test03(self):
        self.assertEqual("abcabccdcdcdef",get_sol().decodeString("2[abc]3[cd]ef"))
    def test04(self):
        self.assertEqual("abccdcdcdxyz",get_sol().decodeString("abc3[cd]xyz"))
    def test05(self):
        self.assertEqual("accaccaccaccaccacc",get_sol().decodeString("3[a2[c]]3[a2[c]]"))
    def test06(self):
        self.assertEqual("leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode",get_sol().decodeString("100[leetcode]"))
    def test07(self):
        self.assertEqual("fef",get_sol().decodeString("1[f]ef"))
    def test08(self):
        self.assertEqual("pqeeeepqeeeeef",get_sol().decodeString("2[pq4[e]]ef"))
    def test09(self):
        self.assertEqual("yyyy", get_sol().decodeString("2[2[y]]"))
    def test10(self):
        self.assertEqual("yypqyypqe", get_sol().decodeString("2[2[y]pq]e"))
    def test11(self):
        self.assertEqual("yypqjkjkjkjkjkjkjkjkyypqjkjkjkjkjkjkjkjke", get_sol().decodeString("2[2[y]pq4[2[jk]]]e"))
    def test12(self):
        self.assertEqual("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",get_sol().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
