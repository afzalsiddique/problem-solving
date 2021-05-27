import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # backtracking
    maxx=0
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        def backtrack(start,path):
            if len(path)>self.maxx:
                self.maxx=len(path)

            for i in range(start,n):
                sett = set(arr[i])
                if len(arr[i]) != len(sett): continue
                if path & sett: continue # https://stackoverflow.com/questions/16696065/is-there-a-difference-between-and-and-with-respect-to-python-sets
                backtrack(i+1,path | sett)
        backtrack(0,set())
        return self.maxx

class Solution2:
    # wrong
    # lis
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        dp = [set() for _ in range(n)]
        li = [set() for _ in range(n)]
        for i in range(n):
            for c in arr[i]:
                if c not in li[i]:
                    li[i].add(c)
                    dp[i].add(c)
                else:
                    li[i]=set()
                    dp[i]=set()
                    break

        for i in range(n):
            for j in range(i):
                before = set(dp[i])
                after = set(dp[i])
                for c in arr[j]:
                    if c not in dp[i]:
                        after.add(c)
                    else:
                        after=set()
                        break
                dp[i] = max(after,before,key=lambda x:len(x))
        sett = max(dp,key=lambda x:len(x))
        return len(sett)
class tester(unittest.TestCase):
    def test1(self):
        arr = ["un","iq","ue"]
        Output= 4
        self.assertEqual(Output,get_sol().maxLength(arr))
    def test2(self):
        arr = ["cha","r","act","ers"]
        Output= 6
        self.assertEqual(Output,get_sol().maxLength(arr))
    def test3(self):
        arr = ["abcdefghijklmnopqrstuvwxyz"]
        Output= 26
        self.assertEqual(Output,get_sol().maxLength(arr))
    def test4(self):
        arr = ["a", "abc", "d", "de", "def"]
        Output= 6
        self.assertEqual(Output,get_sol().maxLength(arr))
    def test5(self):
        arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
        Output= 16
        self.assertEqual(Output,get_sol().maxLength(arr))
    def test6(self):
        arr = ["yy","bkhwmpbiisbldzknpm"]
        Output= 0
        self.assertEqual(Output,get_sol().maxLength(arr))
