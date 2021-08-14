import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxDiff(self, num: int) -> int:
        maxx=list(str(num))
        n=len(maxx)
        if maxx[0]!='9':
            changing_dig=maxx[0]
            for i in range(len(maxx)):
                if maxx[i]==changing_dig:
                    maxx[i]='9'
        else:
            i=0
            while i<n and maxx[i]=='9':
                i+=1
            if i<n:
                changing_dig=maxx[i]
                while i<n:
                    if maxx[i]==changing_dig:
                        maxx[i]='9'
                    i+=1

        minn=list(str(num))
        if minn[0]!='1':
            changing_dig=minn[0]
            for i in range(len(minn)):
                if minn[i]==changing_dig:
                    minn[i]='1'
        else:
            i=0
            while i<n and (minn[i]=='1' or minn[i]=='0'):
                i+=1
            if i<n:
                changing_dig=minn[i]
                while i<n:
                    if minn[i]==changing_dig:
                        minn[i]='0'
                    i+=1
        # print(maxx)
        # print(minn)
        return int(''.join(maxx))-int(''.join(minn))

class MyTestCase(unittest.TestCase):
    def test_1(self):
        num = 555
        Output= 888
        self.assertEqual(Output, get_sol().maxDiff(num))
    def test_2(self):
        num = 9
        Output= 8
        self.assertEqual(Output, get_sol().maxDiff(num))
    def test_3(self):
        num = 123456
        Output= 820000
        self.assertEqual(Output, get_sol().maxDiff(num))
    def test_4(self):
        num = 10000
        Output= 80000
        self.assertEqual(Output, get_sol().maxDiff(num))
    def test_5(self):
        num = 9288
        Output= 8700
        self.assertEqual(Output, get_sol().maxDiff(num))
    def test_6(self):
        num = 1101057
        Output= 8808050
        self.assertEqual(Output, get_sol().maxDiff(num))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):