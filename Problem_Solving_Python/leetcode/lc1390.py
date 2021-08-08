import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find_divisors(num):
            divisors=set()
            for i in range(1,int(math.sqrt(num)+1)):
                if len(divisors)>4: break
                if not num%i:
                    divisors.add(i)
                    divisors.add(num//i)
            return sum(divisors) if len(divisors)==4 else 0

        res=0
        for num in nums: res += find_divisors(num)
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        nums = [21,4,7]
        Output= 32
        self.assertEqual(Output,get_sol().sumFourDivisors(nums))
    def test_2(self):
        nums = [1,2,3,4,5,6,7,8,9,10]
        Output= 45
        self.assertEqual(Output,get_sol().sumFourDivisors(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
