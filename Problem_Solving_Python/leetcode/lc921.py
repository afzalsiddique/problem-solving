import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        cnt=0
        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st: st.pop()
                else: cnt+=1
        return cnt+len(st)

class MyTestCase(unittest.TestCase):
    def test_01(self):
        Input= "())"
        Output= 1
        self.assertEqual(Output, get_sol_obj().minAddToMakeValid(Input))
    def test_02(self):
        Input= "((("
        Output= 3
        self.assertEqual(Output, get_sol_obj().minAddToMakeValid(Input))
    def test_03(self):
        Input= "()"
        Output= 0
        self.assertEqual(Output, get_sol_obj().minAddToMakeValid(Input))
    def test_04(self):
        Input= "()))(("
        Output= 4
        self.assertEqual(Output, get_sol_obj().minAddToMakeValid(Input))
    def test_05(self):
        Input= "(()())(("
        Output= 2
        self.assertEqual(Output, get_sol_obj().minAddToMakeValid(Input))
