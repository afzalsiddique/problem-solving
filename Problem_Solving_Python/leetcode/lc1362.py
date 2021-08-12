import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def get_divisors(num:int):
            li=[]
            for i in range(1,int(math.sqrt(num))+1):
                if not num%i:
                    li.append(i)
                    li.append(num//i)
            return li

        li1=get_divisors(num+1)
        li2=get_divisors(num+2)
        if abs(li1[-1]-li1[-2])<abs(li2[-1]-li2[-2]):
            return [li1[-1],li1[-2]]
        return [li2[-1],li2[-2]]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        num = 8
        Output= [3,3]
        self.assertEqual(Output, get_sol().closestDivisors(num))
    def test_2(self):
        num = 123
        Output= [5,25]
        self.assertEqual(Output, get_sol().closestDivisors(num))
    def test_3(self):
        num = 999
        Output= [40,25]
        self.assertEqual(Output, get_sol().closestDivisors(num))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):