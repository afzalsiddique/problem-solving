import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol_obj(): return Solution()

class Solution:
    # https://www.youtube.com/watch?v=pDyh9VOMWgI&t=548s
    def maximumSwap(self, num: int) -> int:
        li = list(map(int, str(num)))
        index = {x:i for i,x in enumerate(li)}
        for i,x in enumerate(li):
            for y in reversed(range(10)):
                if y in index and index[y]>i and y>x:
                    li[i],li[index[y]] = li[index[y]],li[i]
                    return int(''.join(map(str,li)))
        return num
class Solution2:
    def maximumSwap(self, num: int) -> int:
        li = list(str(num))
        temp = li[:]
        i=0
        while temp:
            maxx = max(temp)
            if maxx!=li[i]:
                break
            temp.remove(maxx)
            i+=1
        if not temp: return num
        idx=li[::-1].index(maxx) # get the last max if multiple. that's why reversed
        idx = len(li)-1-idx
        li[i],li[idx]=li[idx],li[i]
        li = ''.join(li)
        li = int(li)
        return li

# wrong, heap
class Solution3:
    def maximumSwap(self, num: int) -> int:
        temp = str(num)
        li=[int(temp[i]) for i in range(len(temp))]
        pq = [(-li[i],i) for i in range(len(li))]
        heapify(pq)
        for i in range(len(li)):
            _,idx = heappop(pq)
            if idx==i or li[idx]==li[i]: continue
            li[i],li[idx] = li[idx],li[i]
            return int(''.join(list(map(str,li))))
        return num

class tester(unittest.TestCase):
    def test1(self):
        Input = 0
        Output = 0
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test2(self):
        Input = 1
        Output = 1
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test3(self):
        Input = 98
        Output = 98
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test4(self):
        Input = 89
        Output = 98
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test5(self):
        Input = 88
        Output = 88
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test6(self):
        Input = 2736
        Output = 7236
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test7(self):
        Input = 9973
        Output = 9973
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test8(self):
        Input = 999
        Output = 999
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test9(self):
        Input = 98368
        Output = 98863
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test10(self):
        Input = 115
        Output = 511
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test11(self):
        Input =  10909091
        Output = 90909011
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test12(self):
        Input = 99901
        Output = 99910
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
    def test13(self):
        Input = 43456
        Output = 63454
        self.assertEqual(Output,get_sol_obj().maximumSwap(Input))
