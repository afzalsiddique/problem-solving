import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:
        LARGEST=2147483647
        n=len(s)
        self.res=[]
        path=[]
        def h(start):
            if start==n and len(path)>=3: self.res=path[:]
            for i in range(start,n):
                first = s[start:i+1]
                if len(first)>1 and first[0]=='0': # leading zero but not the number '0' itself
                    # continue
                    break
                first=int(first)
                if first>LARGEST: break # checking if fits in a 32 bit signed integer
                if len(path)<=1:
                    path.append(int(first))
                elif first==path[-1]+path[-2]:
                    path.append(int(first))
                else:
                    continue
                h(i+1)
                path.pop()

        h(0)
        return self.res
class tester(unittest.TestCase):
    def test_1(self):
        num = "123456579"
        Output= [123,456,579]
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    def test_2(self):
        num = "11235813"
        Output= [1,1,2,3,5,8,13]
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    def test_3(self):
        num = "112358130"
        Output= []
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    def test_4(self):
        num = "0123"
        Output= []
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    def test_5(self):
        num = "1101111"
        Output= [110, 1, 111]
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    def test_6(self):
        num = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
        Output= []
        self.assertEqual(Output, get_sol().splitIntoFibonacci(num))
    # def test_7(self):
    # num = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    # Output= [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
    # self.assertEqual(Output, get_sol().splitIntoFibonacci(num))

    # def test_8(self):
