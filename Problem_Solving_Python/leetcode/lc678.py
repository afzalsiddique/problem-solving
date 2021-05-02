import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# greedy
# time O(n) space O(1)
class Solution:
    # https://www.youtube.com/watch?v=2H9gMIIGyvY
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for c in s:
            if c in '(*':
                balance+=1
            else:
                balance-=1
            if balance<0: return False
        if balance==0: return True
        balance = 0
        for i,c in enumerate(reversed(s)):
            if c in '*)':
                balance+=1
            else:
                balance-=1
            if balance<0: return False
        return True


# stack
# time O(n) space O(n)
class Solution2:
    # https://www.youtube.com/watch?v=KuE_Cn3xhxI
    def checkValidString(self, s: str) -> bool:
        st_open,st_star=[],[]
        for i,c in enumerate(s):
            if c=='(':
                st_open.append(i)
            elif c==')':
                if not st_open and not st_star: return False
                if st_open:
                    st_open.pop()
                elif st_star:
                    st_star.pop()
            elif c=='*':
                st_star.append(i)

        if not st_open: return True
        if st_open and not st_star: return False
        while st_open:
            temp = st_open.pop()
            if not st_star: return False
            if st_star[-1] < temp: return False
            st_star.pop()
        return True
# backtracking
# TLE
class Solution3:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        def helper(i, path):
            if i==n:
                temp = ''.join(path)
                if self.valid(temp):
                    return True
                return False
            ans = False
            if s[i]== '*':
                ans |= helper(i + 1, path+['('])
                ans |= helper(i + 1, path+[')'])
                ans |= helper(i + 1, path+[''])
            else:
                ans |= helper(i+1,path+[s[i]])
            return ans

        return helper(0,[])

    def valid(self,s):
        st=[]
        for c in s:
            if c=='(':
                st.append(c)
            else:
                if not st: return False
                st.pop()
        return True if not st else False



def get_sol_obj():
    return Solution()
class tester(unittest.TestCase):
    def test2(self):
        s = "()"
        Output= True
        self.assertEqual(Output,get_sol_obj().checkValidString(s))
    def test3(self):
        s = "(*)"
        Output= True
        self.assertEqual(Output,get_sol_obj().checkValidString(s))
    def test4(self):
        s = "(*))"
        Output= True
        self.assertEqual(Output,get_sol_obj().checkValidString(s))
    def test5(self):
        s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        Output= False
        self.assertEqual(Output,get_sol_obj().checkValidString(s))
