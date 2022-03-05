import unittest
from collections import deque
from typing import List
def get_sol(): return Solution()


class Solution:
    # time: O(n) # memory: O(1)
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

class Solution2:
    # time: O(n) # memory: O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        li1=[] # index of opening braces which are invalid
        li2=[] # index of closing braces which are invalid
        for i,x in enumerate(s):
            if x=='(':
                li1.append(i)
            elif x==')':
                if li1:
                    li1.pop()
                else:
                    li2.append(i)
        res=[]
        i,j=0,0
        for k,x in enumerate(s):
            if i<len(li1) and k==li1[i]:
                i+=1
                continue
            if j<len(li2) and k==li2[j]:
                j+=1
                continue
            res.append(x)
        return ''.join(res)
class MyTestCase(unittest.TestCase):
    def test_01(self):
        s = "lee(t(c)o)de)"
        Output= "lee(t(c)o)de"
        self.assertEqual(Output, get_sol().minRemoveToMakeValid(s))
    def test_02(self):
        s = "a)b(c)d"
        Output= "ab(c)d"
        self.assertEqual(Output, get_sol().minRemoveToMakeValid(s))
    def test_03(self):
        s = "))(("
        Output= ""
        self.assertEqual(Output, get_sol().minRemoveToMakeValid(s))
    def test_04(self):
        s = "(a(b(c)d)"
        Output= "a(b(c)d)"
        self.assertEqual(Output, get_sol().minRemoveToMakeValid(s))
