import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()

class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c,x):
            return chr(ord(c)+x)
        n = len(s)
        li = list(s)
        for i in range(1,n,2):
            li[i]=shift(li[i-1],int(li[i]))
        return ''.join(li)


class tester(unittest.TestCase):
    def test1(self):
        s = "a1c1e1"
        Output= "abcdef"
        self.assertEqual(Output,get_sol_obj().replaceDigits(s))
    def test2(self):
        s = "a1b2c3d4e"
        Output= "abbdcfdhe"
        self.assertEqual(Output,get_sol_obj().replaceDigits(s))
    def test3(self):
        self.assertEqual(Output,get_sol_obj().func(Input))
    def test4(self):
        self.assertEqual(Output,get_sol_obj().func(Input))
