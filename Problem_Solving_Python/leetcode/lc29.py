from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    def divide(self, A: int, B: int) -> int:
        if A == -2147483648 and B==-1: return 2147483647
        a=abs(A)
        b=abs(B)
        res=0
        print('B:',b)
        while a-b>=0:
            x=0
            while True:
                tmp=(b<<x<<1) # tmp: 2b,4b,8b,16b. "<<1" so that it does not start from b
                print(tmp)
                if not a-(b<<x<<1)>=0:
                    break
                x+=1
            res+= 1<<x
            print()
            a-=b<<x
        return res if (A > 0) == (B > 0) else -res


class Solution4:
    # https://www.youtube.com/watch?v=htX69j1jf5U
    def divide(self, dividend: int, divisor: int) -> int:

        def helper(dividend, divisor):
            if dividend<0 and divisor<0:
                return helper(-dividend, -divisor)
            if dividend<0 and divisor>0:
                quotient, dividend = helper(-dividend, divisor)
                return -quotient, dividend
            if dividend>0 and divisor<0:
                quotient, dividend = helper(dividend, -divisor)
                return -quotient, dividend

            if dividend<divisor:
                return 0, dividend
            else:
                dividend -= divisor
                quotient = 1
                temp, new_dividend = helper(dividend, 2*divisor)
                quotient += 2 * temp
                if new_dividend>=divisor:
                    new_dividend-=divisor
                    quotient+=1
            return quotient, new_dividend
        quotient = helper(dividend, divisor)[0]
        return min(max(-2147483648, quotient), 2147483647) # make sure that -2147483648 <= quotient <= 2147483647.

class Solution3:
    # TLE. binary search with power
    def divide(self, dividend: int, divisor: int) -> int:
        def recur(dividend:int,divisor:int):
            if divisor>dividend:
                return 0
            lo,hi=1,32
            while lo<=hi:
                power=(lo+hi)>>1
                if pow(divisor,power)<=dividend:
                    lo=power+1
                else:
                    hi=power-1
            res=lo-1
            part1=int(pow(divisor,res-1))
            part2=int(recur(dividend-pow(divisor,res),divisor))
            return part1+part2

        sign=1 if dividend>0 and divisor>0 or dividend<0 and divisor<0 else -1
        return recur(abs(dividend),abs(divisor))*sign
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().divide(10, 3))
    def test02(self):
        self.assertEqual(2, get_sol().divide( 7,  3))
    def test03(self):
        self.assertEqual(11, get_sol().divide(35, 3))
    def test04(self):
        self.assertEqual(-2, get_sol().divide( 7,  -3))
    def test05(self):
        self.assertEqual(0, get_sol().divide( 0,  1))
    def test06(self):
        self.assertEqual(1, get_sol().divide( 1,  1))
    def test07(self):
        self.assertEqual(-2147483648, get_sol().divide(-2147483648, 1))
    def test08(self):
        self.assertEqual(4, get_sol().divide(4, 1))
    def test09(self):
        self.assertEqual(4, get_sol().divide(8,2))
    def test10(self):
        self.assertEqual(2147483647, get_sol().divide(-2147483648, -1))
    def test11(self):
        self.assertEqual(-2,get_sol().divide(7,-3))
    def test12(self):
        self.assertEqual(1,get_sol().divide(2, 2))
