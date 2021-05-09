import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = [(log[0],True) for log in logs]
        end = [(log[1],False) for log in logs]
        li = start+end
        li.sort()
        cnt=0
        maxx=0
        maxx_year=start[0]
        for year,start in li:
            if start:
                cnt+=1
                if cnt>maxx:
                    maxx=cnt
                    maxx_year=year
            else:
                cnt-=1
        return maxx_year



class tester(unittest.TestCase):
    def test01(self):
        logs = [[1993,1999],[2000,2010]]
        Output= 1993
        self.assertEqual(Output,get_sol().maximumPopulation(logs))
    def test02(self):
        logs = [[1950,1961],[1960,1971],[1970,1981]]
        Output= 1960
        self.assertEqual(Output,get_sol().maximumPopulation(logs))
    def test03(self):
        n=2
        Output= 91
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
    def test04(self):
        n=3
        Output= 739
        self.assertEqual(Output,get_sol().countNumbersWithUniqueDigits(n))
