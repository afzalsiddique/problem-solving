import itertools;from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution3:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def parse(path):
            res=[]
            i=0
            while i<len(path):
                num=0
                while i<len(path) and '0'<=path[i]<='9':
                    num=num*10+int(path[i])
                    i+=1
                res.append(num)

                if i<len(path) and not '0'<=path[i]<='9':
                    res.append(path[i])
                    i+=1
            return res

        def dfs(path):
            if len(path)==1: return [path[0]]
            res=[]
            for i in range(len(path)):
                if str(path[i]) in '+-*':
                    ans1=dfs(path[:i])
                    ans2=dfs(path[i+1:])
                    for x in itertools.product(ans1,ans2):
                        a,b=x[0],x[1]
                        if path[i]=='-': res.append(a-b)
                        elif path[i]=='+': res.append(a+b)
                        else: res.append(a*b)
            return res

        path = parse(expression)
        return dfs(path)
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
                ans1=helper(expr[:i])
                ans2=helper(expr[i+1:])
                # for a1,a2 in product(ans1,ans2):
                #     if expr[i]=='+': res.append(a1+a2)
                #     elif expr[i]=='-': res.append(a1-a2)
                #     elif expr[i]=='*': res.append(a1*a2)
                for a1 in ans1:
                    for a2 in ans2:
                        if expr[i]=='+': res.append(a1+a2)
                        elif expr[i]=='-': res.append(a1-a2)
                        elif expr[i]=='*': res.append(a1*a2)
            return res

        return helper(expression)
class Solution2:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.helper(input)

    def helper(self, str):
        li = []
        for i in range(len(str)):
            if str[i] == '*' or str[i] == '-' or str[i] == '+':
                left = self.helper(str[:i])
                right = self.helper(str[i + 1:])
                for item_left in left:
                    for item_right in right:
                        if str[i] == '*':
                            li.append(int(item_left) * int(item_right))
                        elif str[i] == '+':
                            li.append(int(item_left) + int(item_right))
                        else:
                            li.append(int(item_left) - int(item_right))
        if len(li) == 0:
            return [int(str)]

        return li

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([0,2], sorted(get_sol().diffWaysToCompute("2-1-1")))
    def test02(self):
        self.assertEqual([-34,-14,-10,-10,10], sorted(get_sol().diffWaysToCompute("2*3-4*5")))
    def test03(self):
        self.assertEqual([-374, -110, -110, 46, 310], sorted(get_sol().diffWaysToCompute("22*3-4*5")))
    def test04(self):
        self.assertEqual([50], sorted(get_sol().diffWaysToCompute("20+30")))
