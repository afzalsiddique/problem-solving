import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(expr):
            found=False
            for c in expr:
                if c=='+' or c=='-' or c=='*':
                    found=True
                    break
            if not found: return [int(expr)]
            res = []
            for i in range(len(expr)):
                if expr[i] not in '+-*': continue
                if expr[i] =='+':
                    ans1=helper(expr[:i])
                    ans2=helper(expr[i+1:])
                    for a1 in ans1:
                        for a2 in ans2:
                            res.append(a1+a2)
                elif expr[i]=='-':
                    ans1=helper(expr[:i])
                    ans2=helper(expr[i+1:])
                    for a1 in ans1:
                        for a2 in ans2:
                            res.append(a1-a2)
                elif expr[i]=='*':
                    ans1=helper(expr[:i])
                    ans2=helper(expr[i+1:])
                    for a1 in ans1:
                        for a2 in ans2:
                            res.append(a1*a2)
            return res

        return helper(expression)

class MyTestCase(unittest.TestCase):
    def test_01(self):
        expression = "2-1-1"
        Output= [0,2]
        self.assertEqual(Output, get_sol_obj().diffWaysToCompute(expression))
    def test_02(self):
        expression = "2*3-4*5"
        Output= [-34,-14,-10,-10,10]
        self.assertEqual(Output, get_sol_obj().diffWaysToCompute(expression))
    def test_03(self):
        expression = "22*3-4*5"
        Output= []
        self.assertEqual(Output, get_sol_obj().diffWaysToCompute(expression))
