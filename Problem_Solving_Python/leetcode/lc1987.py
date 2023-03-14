from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/number-of-unique-good-subsequences/solutions/1431819/java-c-python-dp-4-lines-o-n-time-o-1-space/comments/1064733
    # num         1          0             1                             1
    # end0Count   0          1             1                             1
    # end1Count   1          1             3                             5
    # end0Arr      [ ]        [10]       [10]                        [10]
    # end1Arr      [1]       [1]         [11, 101, 1]          [101, 111, 1011, 11, 1]
    # "1" itself is a valid subsequence, so you'll miss it if you only count "ends0 + ends1".
    # "0" itself is also a valid subsequence, but it will fail with any follow-up bits, like "01", "00", so the solution decides NOT to +1 every time but check if "0" exist in the given string, then simply +1 to the ans if at least one "0" exists.
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        M=10**9+7
        dp=[0,0]
        for c in binary:
            idx=int(c)
            if idx==0: dp[idx]=sum(dp)
            else: dp[idx]=sum(dp)+1
        return (sum(dp)+int('0' in binary))%M
class Solution2:
    def numberOfUniqueGoodSubsequences(self, s: str) -> int:
        M=10**9+7
        n=len(s)
        dp=[0]*2
        dp[ord(s[0])-ord('0')]=1
        for i in range(1,n):
            tmp=sum(x for x in dp)
            idx=ord(s[i])-ord('0')
            if dp[0]!=0:
                dp[idx]=tmp
            else:
                dp[idx]=tmp+1
            dp[idx]%=M
        return sum(dp)%M

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().numberOfUniqueGoodSubsequences("001"))
    def test2(self):
        self.assertEqual(2, get_sol().numberOfUniqueGoodSubsequences("11"))
    def test3(self):
        self.assertEqual(5, get_sol().numberOfUniqueGoodSubsequences("101"))
    def test4(self):
        self.assertEqual(1, get_sol().numberOfUniqueGoodSubsequences("0"))
    def test5(self):
        self.assertEqual(23, get_sol().numberOfUniqueGoodSubsequences("1110001"))
    def test6(self):
        self.assertEqual(846803618, get_sol().numberOfUniqueGoodSubsequences("1100100010101010100100000111110001111001000010000010010111011"))
    # def test7(self):
    # def test8(self):
    # def test9(self):
