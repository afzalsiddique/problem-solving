from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution2()

# a^4567 % k = (a^4560 % k) * (a^7 % k) % k = (a^456 % k)^10 % k * (a^7 % k) % k
# f(a,4567) = f(a, 4560) * f(a, 7) % k = f(f(a, 456),10) * f(a,7)%k;
# https://www.youtube.com/watch?v=bg0P_3UiG5I&t=987s

class Solution:
    # https://leetcode.com/problems/super-pow/discuss/84472/C%2B%2B-Clean-and-Short-Solution
    def superPow(self, a: int, b: List[int]) -> int:
        def pow_mod(a,b): # (a**b)%M
            res = 1
            for i in range(b):
                res *= a%M
                res %= M
            return res
        def f() -> int:
            if not b: return 1
            last_digit = b.pop()
            return pow_mod(f(), 10) * pow_mod(a, last_digit) % M

        M=1337
        return f()
class Solution2:
    # https://leetcode.com/problems/super-pow/discuss/84485/8ms-JAVA-solution-using-fast-power
    # https://leetcode.com/problems/super-pow/discuss/84472/C%2B%2B-Clean-and-Short-Solution
    def superPow(self, a: int, b: List[int]) -> int:
        M=1337
        def normalPow(x, n): # x to the nth power. same as leetcode 50
            if n==0: return 1
            p= normalPow(x, n // 2) % M
            p= (p*p) % M
            return (p*x) % M if n % 2 else p

        a %= M
        result=1
        for i in range(len(b)-1,-1,-1):
            result = (result * normalPow(a,b[i])) % M
            a = normalPow(a, 10)
        return result



class MyTestCase(unittest.TestCase):
    def test1(self):
        a,b = 2,  [3]
        Output= 8
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test2(self):
        a,b = 2,  [1,0]
        Output= 1024
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test3(self):
        a,b = 1,  [4,3,3,8,5,2]
        Output= 1
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test4(self):
        a,b = 2147483647,  [2,0,0]
        Output= 1198
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test5(self):
        a,b = 2147483647,  [2,3,5]
        Output= 1184
        self.assertEqual(Output, get_sol().superPow(a,b))
    def test6(self):
        a,b = 2,  [1,8]
        Output= 92
        self.assertEqual(Output, get_sol().superPow(a,b))
