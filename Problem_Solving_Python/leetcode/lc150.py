from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for x in tokens:
            if x in '*+/-':
                right=st.pop()
                left=st.pop()
                if x=='+': st.append(left+right)
                elif x=='-': st.append(left-right)
                elif x=='*': st.append(right*left)
                else:
                    if right>0 and left>0 or right<0 and left<0:
                        st.append(left//right)
                    else:
                        left=abs(left)
                        right=abs(right)
                        st.append((left//right)*(-1))
            else:
                st.append(int(x))
        return st[-1]
class Solution3:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                right, left = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(left+right)
                elif t == "-":
                    stack.append(left-right)
                elif t == "*":
                    stack.append(left*right)
                else:
                    stack.append(int(float(left)/right))
        return stack.pop()
class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_operator(char):
            if char in '+-*/':
                return True
            return False
        def do_operation(num1,num2,operator):
            if operator=='+':
                return int(num1)+int(num2)
            elif operator=='-':
                return int(num1)-int(num2)
            elif operator=='*':
                return int(num1)*int(num2)
            else:
                # 2/-6 should return 0. but 2//-6 returns -1.
                return int(num1/num2)
                # return int(float(num1)/num2) # this one also works
        st=[]
        ans = int(tokens[0]) # when only one element in tokens
        for item in tokens:
            if is_operator(item):
                num1=st.pop()
                num2=st.pop()
                ans = do_operation(num2,num1,item)
                st.append(ans)
            else:
                st.append(int(item))
        return ans

class mycase(unittest.TestCase):
    def test01(self):
        self.assertEqual(9, get_sol().evalRPN(["2","1","+","3","*"]))
    def test02(self):
        self.assertEqual(6, get_sol().evalRPN(["4","13","5","/","+"]))
    def test03(self):
        self.assertEqual(1, get_sol().evalRPN(["1"]))
    def test04(self):
        self.assertEqual(22, get_sol().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    def test05(self):
        self.assertEqual(2, get_sol().evalRPN(["14","5","/"]))
    def test06(self):
        self.assertEqual(-2, get_sol().evalRPN(["-14","5","/"]))

