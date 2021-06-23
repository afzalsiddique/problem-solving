import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=len(chalk)
        summ = sum(chalk)
        k = k % summ
        i=0
        while k>=0:
            k-=chalk[i]
            i+=1
            if i==n: i=0
        if i==0: return n-1
        return i-1

class tester(unittest.TestCase):
    def test01(self):
        chalk = [5,1,5]
        k = 22
        Output= 0
        self.assertEqual(Output,get_sol().chalkReplacer(chalk, k))
    def test02(self):
        chalk = [10_000 for _ in range(100_000)]
        k = 1_000_000_000
        Output= 0
        self.assertEqual(Output,get_sol().chalkReplacer(chalk, k))
    def test03(self):
        chalk = [30,81,7,99,4,14,70,14,57,23,45,51,87,1,11,14,94,53,74,93,42,88,35,20,72,25,64,7,13,89,74,35,65,24,17,25,14,13,16,98,97,93,59,72,97,79,50,99,32,50,73,62,82,10,93]
        k = 926789742
        Output = 35
        self.assertEqual(Output,get_sol().chalkReplacer(chalk, k))
    def test04(self):
        chalk = [22,86,96,35,62,69,56,33,95,10,38,53,33,90,29,68,85,58,11,49,81,18,32,96,40,75,49,26,60,71,15,94,31,99,12,81,10,19,7,73,35,56,100,15,37,89,58,17,55,62,4,30,68,68,89,62,39,35,16,18,63,73,100,22,46,58,80,77,23,5,52,96,98,21,33,86,81,71,69,72,71,58,17,85,70,22,84,94,75,51,60,81,12,22,13,33,53,58]
        k = 134221332
        Output= 97
        self.assertEqual(Output,get_sol().chalkReplacer(chalk, k))
