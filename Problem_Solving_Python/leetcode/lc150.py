from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
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
    def test1(self):
        self.assertEqual(9, Solution().evalRPN(["2","1","+","3","*"]))
    def test2(self):
        self.assertEqual(6, Solution().evalRPN(["4","13","5","/","+"]))
    def test3(self):
        self.assertEqual(1, Solution().evalRPN(["1"]))
    def test4(self):
        self.assertEqual(22, Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
