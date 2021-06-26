import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res=[]
        def helper(path,n:int):
            if n==0:
                res.append(''.join(list(map(str,path))))
                # res.append(path[:])
                return
            for i in range(0,10):
                if abs(path[-1]-i)==k:
                    helper(path+[i],n-1)

        for i in range(1,10):
            helper([i],n-1)
        res=list(map(int,res))
        return res


class tester(unittest.TestCase):
    def test01(self):
        n = 3
        k = 7
        Output= [181,292,707,818,929]
        self.assertEqual(Output,get_sol().numsSameConsecDiff(n,k))
    def test02(self):
        n = 2
        k = 1
        Output= [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
        self.assertEqual(Output,get_sol().numsSameConsecDiff(n,k))
    def test03(self):
        n = 2
        k = 0
        Output= [11,22,33,44,55,66,77,88,99]
        self.assertEqual(Output,get_sol().numsSameConsecDiff(n,k))
    def test04(self):
        n = 2
        k = 2
        Output= [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
        self.assertEqual(Output,get_sol().numsSameConsecDiff(n,k))
