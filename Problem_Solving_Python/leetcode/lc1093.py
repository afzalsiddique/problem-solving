import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n=256
        no_of_elements=sum(count)

        def get_max():
            i=n-1
            max_element=float('-inf')
            while i>=0:
                if count[i]!=0:
                    max_element=i
                    break
                i-=1
            return max_element*1.0
        def get_min():
            i=0
            min_element=float('inf')
            while i<n:
                if count[i]!=0:
                    min_element=i
                    break
                i+=1
            return min_element*1.0
        def get_mode():
            mode=float('-inf')
            freq=float('-inf')
            i=0
            for i in range(n):
                if count[i]>freq:
                    freq=count[i]
                    mode=i
            return mode*1.0
        def get_avg():
            total=sum(i*count[i] for i in range(n))
            return total/no_of_elements
        def get_median():
            for i in range(n-1):
                count[i + 1] += count[i] # cumulative sum
            median1 = bisect_right(count, (no_of_elements - 1) // 2)
            median2 = bisect_right(count, no_of_elements // 2)
            median = (median1 + median2) / 2.0
            return median

        minn=get_min()
        maxx=get_max()
        avg=get_avg()
        mode=get_mode()
        med=get_median()
        return [minn,maxx,avg,med,mode]



class MyTestCase(unittest.TestCase):
    def test_1(self):
        count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Output= [1.00000,3.00000,2.37500,2.50000,3.00000]
        self.assertEqual(Output, get_sol().sampleStats(count))
    def test_2(self):
        count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Output= [1.00000,4.00000,2.18182,2.00000,1.00000]
        self.assertEqual(Output, get_sol().sampleStats(count))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):