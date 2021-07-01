import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # important observation - 0 <= arr[i] <= 100
    # https://www.youtube.com/watch?v=jZcAldZP1ag
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9+7
        count = Counter(arr)
        res=0
        for i in range(100+1):
            for j in range(100+1):
                k=target-i-j
                if not 0<=k<=100: continue # according to constraint
                if i==j==k:
                    n=count[i]
                    nc3 = n*(n-1)*(n-2)//6 # combination formula
                    res+=nc3
                elif i==j and j!=k: # any two of them are equal and the third is not.
                    n=count[i]
                    nc2=n*(n-1)//2 # combination formula
                    res+=nc2 * count[k]
                elif i<j<k:
                    res+=count[i]*count[j]*count[k]
                res%=MOD
        return res
class Solution2:
    # important observation - 0 <= arr[i] <= 100
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n=len(arr)
        res=0
        MOD=10**9+7
        for i in range(n-1):
            count=[0 for _ in range(101)]
            for j in range(i+1,n):
                new_target=target-arr[i]-arr[j]
                if 0 <= new_target <= 100 and count[new_target]>0:
                    res+=count[new_target]
                    res%=MOD
                count[arr[j]]+=1
        return res


class tester(unittest.TestCase):
    def test01(self):
        arr = [1,1,2,2,3,3,4,4,5,5]
        target = 8
        Output= 20
        self.assertEqual(Output,get_sol().threeSumMulti(arr,target))
    def test02(self):
        arr = [1,1,2,2,2,2]
        target = 5
        Output= 12
        self.assertEqual(Output,get_sol().threeSumMulti(arr,target))
    # def test03(self):
    # def test04(self):
    # def test05(self):
