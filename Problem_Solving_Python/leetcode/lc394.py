from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = []
        for c in s:
            if c == ']':
                temp = []
                while st[-1]!='[':
                    temp.append(st.pop())
                temp.reverse()
                st.pop() # pop '['
                n = []
                while True:
                    if not st:break
                    if st[-1] not in "0123456789":break
                    n.append(st.pop())
                n.reverse()
                n = "".join(n)
                n = int(n)
                temp = "".join(temp)*n
                st.append(temp)
            else:
                st.append(c)
        for x in st:
            res.append(x)
        return "".join(res)
class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual("aaabcbc",Solution().decodeString("3[a]2[bc]"))
    def test2(self):
        self.assertEqual("accaccacc",Solution().decodeString("3[a2[c]]"))
    def test3(self):
        self.assertEqual("abcabccdcdcdef",Solution().decodeString("2[abc]3[cd]ef"))
    def test4(self):
        self.assertEqual("abccdcdcdxyz",Solution().decodeString("abc3[cd]xyz"))
    def test5(self):
        self.assertEqual("accaccaccaccaccacc",Solution().decodeString("3[a2[c]]3[a2[c]]"))
    def test6(self):
        self.assertEqual("leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode",Solution().decodeString("100[leetcode]"))
