from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for c in s:
            if c==']':
                li=[]
                while st and 'a'<=st[-1]<='z':
                    li.append(st.pop())
                li.reverse()
                st.pop()
                num=[]
                while st and '0'<=st[-1]<='9':
                    num.append(st.pop())
                num.reverse()
                num=int(''.join(num) if num else '1')
                st.append(''.join(li)*num)
            else:
                st.append(c)
        return ''.join(st)

class Correct:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == ']':
                temp = []
                while st[-1]!='[': # pop everything inside []
                    temp.append(st.pop())
                temp.reverse()
                st.pop() # pop '['
                cnt = []
                while st and st[-1] in "0123456789": # pop the num
                    cnt.append(st.pop())
                cnt.reverse()
                cnt = int("".join(cnt))
                temp = "".join(temp)*cnt
                st.append(temp)
            else:
                st.append(c)
        return "".join(st)


class Tester(unittest.TestCase):
    def test01(self):
        a="2[2[y]pq]ef"
        self.assertEqual(Correct().decodeString(a), Solution().decodeString(a))
