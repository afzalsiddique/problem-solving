from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution3()

# https://leetcode.com/problems/remove-invalid-parentheses/solution/182911
class Solution:
    # https://www.youtube.com/watch?v=ubKTA5WAaXM
    def removeInvalidParentheses(self, s):
        self.ans = set()
        self.min_removed = float("inf")

        def dfs(i, left, right, removed, cur):
            if i == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[i] != "(" and s[i] != ")": # char
                    dfs(i + 1, left, right, removed, cur + s[i])
                else:
                    dfs(i + 1, left, right, removed + 1, cur)
                    if s[i] == "(":
                        dfs(i + 1, left + 1, right, removed, cur + "(")
                    elif s[i] == ")" and right < left:
                        dfs(i + 1, left, right + 1, removed, cur + ")")

        dfs(0, 0, 0, 0, "")
        return list(self.ans)

class Solution2:
    def removeInvalidParentheses(self, s):
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        self.ans = set()

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(cur)
            else:
                if s[depth] == "(" and left_rem > 0:
                    dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
                elif s[depth] == "(":
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
                elif s[depth] == ")" and right < left:
                    dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

        dfs(0, 0, 0, left, right, "")
        return list(self.ans)

class Solution3:
    # TLE.bitmask
    def minNumRemove(self,s:str):
        bal=0
        res=0
        for c in s:
            if c=='(':
                bal-=1
            elif c==')':
                if not bal: res+=1
                else: bal+=1
        return res+abs(bal)
    def balanced(self,s:str): return self.minNumRemove(s)==0
    def countSetBits(self,mask):
        cnt=0
        while mask:
            mask&=mask-1
            cnt+=1
        return cnt
    def is_on(self,mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
    def getString(self,s,mask):
        li = [s[i] for i in range(25) if self.is_on(mask,i)]
        return ''.join(li)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n=len(s)
        k = self.minNumRemove(s)
        res=set()
        lengthAfterRemoving = n-k
        for mask in range(1<<n):
            if self.countSetBits(mask)==lengthAfterRemoving:
                myString=self.getString(s,mask)
                if self.balanced(myString):
                    res.add(myString)
        return list(res)
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted(["()()()","(())()"]), sorted(get_sol().removeInvalidParentheses("()())()")))
    def test02(self):
        self.assertEqual(sorted(["(a)()()","(a())()"]), sorted(get_sol().removeInvalidParentheses("(a)())()")))
    def test03(self):
        self.assertEqual([""], get_sol().removeInvalidParentheses(")("))
    def test04(self):
        self.assertEqual(["n"], get_sol().removeInvalidParentheses("n"))
    def test05(self):
        self.assertEqual(["()"], get_sol().removeInvalidParentheses("()("))
    def test06(self):
        self.assertEqual(sorted(['z(((fp)))g', 'z((fp))()g', '((zfp))()g', '(z(fp))()g', '(z((fp)))g', '((z(fp)))g']), sorted(get_sol().removeInvalidParentheses("((z(((fp))()((((((g(")))
