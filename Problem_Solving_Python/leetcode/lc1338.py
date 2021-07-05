import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n)
    # space O(n)
    # similar to bucket sort
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        count = Counter(arr)
        li=[0]*(n+1) # idx denotes freq
        for x in count:
            freq=count[x]
            li[freq]+=1
        cnt=0
        len_of_set=0
        i=n
        while cnt<math.ceil(n/2):
            while cnt<math.ceil(n/2) and li[i]!=0:
                li[i]-=1
                len_of_set+=1
                cnt+=i
            i-=1
        return len_of_set
class Solution2:
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        count = Counter(arr)
        ans=0
        cnt=0
        for x in sorted(count,key=count.get,reverse=True):
            ans+=count[x]
            cnt+=1
            if n%2==1:
                if ans>n//2: break
            else:
                if ans>=n//2: break

        return cnt
class MyTestCase(unittest.TestCase):
    def test_01(self):
        arr = [3,3,3,3,5,5,5,2,2,7]
        Output= 2
        self.assertEqual(Output,get_sol().minSetSize(arr))
    def test_02(self):
        arr = [7,7,7,7,7,7]
        Output= 1
        self.assertEqual(Output,get_sol().minSetSize(arr))
    def test_03(self):
        arr = [1,9]
        Output= 1
        self.assertEqual(Output,get_sol().minSetSize(arr))
    def test_04(self):
        arr = [1000,1000,3,7]
        Output= 1
        self.assertEqual(Output,get_sol().minSetSize(arr))
    def test_05(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        Output= 5
        self.assertEqual(Output,get_sol().minSetSize(arr))
    # def test_06(self):
    # def test_07(self):
    # def test_08(self):