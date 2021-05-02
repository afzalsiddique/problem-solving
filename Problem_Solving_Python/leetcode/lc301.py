import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


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
                if s[i] != "(" and s[i] != ")":
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

class tester(unittest.TestCase):
    def test_10(self):
        s = "()())()"
        Output= ["()()()","(())()"]
        self.assertEqual(Output, Solution().removeInvalidParentheses(s))
    def test_11(self):
        s = "(a)())()"
        Output= ["(a)()()","(a())()"]
        self.assertEqual(Output, Solution().removeInvalidParentheses(s))
    def test_12(self):
        s = ")("
        Output= [""]
        self.assertEqual(Output, Solution().removeInvalidParentheses(s))
    def test_13(self):
        s = "n"
        Output= ["n"]
        self.assertEqual(Output, Solution().removeInvalidParentheses(s))
    def test_14(self):
        s = "()("
        Output= ["()"]
        self.assertEqual(Output, Solution().removeInvalidParentheses(s))
