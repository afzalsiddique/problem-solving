import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=[]
        cnt=0
        for c in s:
            if c!=')':
                res.append(c)
                if c=='(':
                    cnt-=1
            else:
                if cnt!=0:
                    res.append(c)
                    cnt+=1
        if cnt==0: return ''.join(res)
        new_res = []
        cnt=0
        for c in reversed(res):
            if c!='(':
                new_res.append(c)
                if c==')':
                    cnt-=1
            else:
                if cnt!=0:
                    new_res.append(c)
                    cnt+=1
        if cnt==0: return ''.join(new_res[::-1])
        return ""

class MyTestCase(unittest.TestCase):
    def test_01(self):
        s = "lee(t(c)o)de)"
        Output= "lee(t(c)o)de"
        self.assertEqual(Output, get_sol_obj().minRemoveToMakeValid(s))
    def test_02(self):
        s = "a)b(c)d"
        Output= "ab(c)d"
        self.assertEqual(Output, get_sol_obj().minRemoveToMakeValid(s))
    def test_03(self):
        s = "))(("
        Output= ""
        self.assertEqual(Output, get_sol_obj().minRemoveToMakeValid(s))
    def test_04(self):
        s = "(a(b(c)d)"
        Output= "a(b(c)d)"
        self.assertEqual(Output, get_sol_obj().minRemoveToMakeValid(s))
