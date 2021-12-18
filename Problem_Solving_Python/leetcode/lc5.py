import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                elif s[i]==s[j]:
                    if j-i+1==2:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i+1][j-1]

        # for x in dp: print(x)
        maxx=float('-inf')
        start,end=-1,-1
        for i in range(n):
            for j in range(i,n):
                if dp[i][j]:
                    if j-i+1>maxx:
                        maxx=j-i+1
                        start,end=i,j
        return s[start:end+1]
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
        for i in reversed(range(n-2)):
            for j in range(i+1,n):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True

        maxx = 0
        res = ""
        for i in reversed(range(n)):
            for j in range(i,n):
                if dp[i][j]==True and j-i+1>maxx:
                    maxx = j-i+1
                    res = s[i:j+1]
        return res


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual('aba',get_sol().longestPalindrome('babad'))
    def test_2(self):
        self.assertEqual('a',get_sol().longestPalindrome('a'))
    def test_3(self):
        self.assertEqual('aa',get_sol().longestPalindrome('aa'))
    def test_4(self):
        self.assertEqual('aaa',get_sol().longestPalindrome('aaa'))
    def test_5(self):
        self.assertEqual('bacab',get_sol().longestPalindrome("abacab"))
    def test_6(self):
        self.assertEqual('c',get_sol().longestPalindrome("ac"))
    def test_7(self):
        self.assertEqual('bb',get_sol().longestPalindrome("cbbd"))
    def test_8(self):
        self.assertEqual('aca',get_sol().longestPalindrome("aacabdkacaa"))
    def test_9(self):
        self.assertEqual('oxaxo',get_sol().longestPalindrome("vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"))
