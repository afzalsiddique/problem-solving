import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/cinema-seat-allocation/discuss/546451/Java-Straightforward-solution-(bitwise)
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats2345=int('00000111100',2) # starting couting from the right
        seats6789=int('01111000000',2)
        seats4567=int('00011110000',2)
        def turn_on(jobs,job_id): return jobs | (1<<job_id)
        di=defaultdict(int)
        for r,c in reservedSeats:
            di[r]=turn_on(di[r],c)

        res=0
        for x in di:
            cnt=0
            reserved = di[x]
            if not (reserved&seats2345): # nothing common in between
                cnt+=1
            if not (reserved&seats6789):
                cnt+=1
            if cnt==0 and not (reserved&seats4567):
                cnt+=1
            res+=cnt
        return res + 2 * (n-len(di))
class Solution2:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def turn_off(jobs,job_id): return jobs & ~(1<<job_id)
        def is_on(jobs,job_id): return jobs & (1<<job_id)
        li=[31 for _ in range(n)]
        for r,c in reservedSeats:
            if 2<=c<=3:
                li[r-1]=turn_off(li[r-1],0)
            elif 4<=c<=5:
                li[r-1]=turn_off(li[r-1],1)
            elif 6<=c<=7:
                li[r-1]=turn_off(li[r-1],2)
            elif 8<=c<=9:
                li[r-1]=turn_off(li[r-1],3)

        res=0
        for i in range(n):
            if is_on(li[i],0) and is_on(li[i],1):
                res+=1
                li[i]=turn_off(li[i],0)
                li[i]=turn_off(li[i],1)
            if is_on(li[i],1) and is_on(li[i],2):
                res+=1
                li[i]=turn_off(li[i],1)
                li[i]=turn_off(li[i],2)
            if is_on(li[i],2) and is_on(li[i],3):
                res+=1
                li[i]=turn_off(li[i],2)
                li[i]=turn_off(li[i],3)
        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,reservedSeats = 3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
        Output= 4
        self.assertEqual(Output, get_sol().maxNumberOfFamilies(n,reservedSeats))
    def test_2(self):
        n,reservedSeats = 2, [[2,1],[1,8],[2,6]]
        Output= 2
        self.assertEqual(Output, get_sol().maxNumberOfFamilies(n,reservedSeats))
    def test_3(self):
        n,reservedSeats = 4, [[4,3],[1,4],[4,6],[1,7]]
        Output= 4
        self.assertEqual(Output, get_sol().maxNumberOfFamilies(n,reservedSeats))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):