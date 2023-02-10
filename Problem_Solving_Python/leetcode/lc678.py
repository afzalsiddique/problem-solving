from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # greedy
    # time O(n) space O(1)
    # https://www.youtube.com/watch?v=2H9gMIIGyvY
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for c in s: # assuming imbalance happened because of insufficient opening parenthesis
            if c in '(*': # treat * as opening
                balance+=1
            else:
                balance-=1
            if balance<0: return False # even after treating all stars as opening parenthesis imbalance remains
        if balance==0: return True

        balance = 0
        for c in s[::-1]:
            if c in '*)':
                balance+=1
            else:
                balance-=1
            if balance<0: return False
        return True

class Solution4:
    def checkValidString(self, s: str) -> bool:
        if s[-1]=='(': return False
        if s[0]==')': return False
        bal = 0
        star=0
        for c in s:
            if bal<0 and star<abs(bal):
                return False
            if c=='(':
                bal+=1
            elif c==')':
                bal-=1
            else:
                star+=1
        if bal>0 and star<bal:
            return False

        bal=0
        star=0
        for c in s[::-1]:
            if bal>0 and star<abs(bal):
                return False
            if c=='(':
                bal+=1
            elif c==')':
                bal-=1
            else:
                star+=1
        if bal<0 and star<abs(bal):
            return False

        return True

class Solution2:
    # stack
    # time O(n) space O(n)
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
class Solution3:
    # backtracking
    # TLE
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




class Tester(unittest.TestCase):
    def test02(self):
        self.assertEqual(True, get_sol().checkValidString("()"))
    def test03(self):
        self.assertEqual(True, get_sol().checkValidString("(*)"))
    def test04(self):
        self.assertEqual(True, get_sol().checkValidString("(*))"))
    def test05(self):
        self.assertEqual(False, get_sol().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
    def test06(self):
        self.assertEqual(True,get_sol().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
    def test07(self):
        self.assertEqual(True,get_sol().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))"))
    def test08(self):
        self.assertEqual(True,get_sol().checkValidString("**(*"))
    def test09(self):
        self.assertEqual(False,get_sol().checkValidString("***((("))
    def test10(self):
        self.assertEqual(False,get_sol().checkValidString("(****("))
    def test11(self):
        self.assertEqual(False,get_sol().checkValidString("((**))(("))
    def test12(self):
        self.assertEqual(False,get_sol().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))))((*(((((**(**)"))
    def test13(self):
        self.assertEqual(False,get_sol().checkValidString("(((((*(((*(*******)))((*(((((****"))
    def test14(self):
        self.assertEqual(False,get_sol().checkValidString("((*(((*(****))(("))
    def test15(self):
        self.assertEqual(False,get_sol().checkValidString("((*"))
    def test16(self):
        self.assertEqual(False,get_sol().checkValidString("*))"))
