import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=Fqal25ZgEDo
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k=len(nums)
        pq=[]
        maxx=float('-inf')
        for i in range(k):
            heappush(pq,[nums[i][0],0,i]) # val, idx, row_no
            maxx=max(maxx,nums[i][0])

        lo,hi=float('inf'),float('-inf')
        res=float('inf')
        while len(pq)==k:
            val,idx,row_no=heappop(pq)
            if maxx-val<res:
                res=maxx-val
                lo,hi=val,maxx
            if idx+1<len(nums[row_no]):
                heappush(pq,[nums[row_no][idx+1],idx+1,row_no])
                maxx=max(maxx,nums[row_no][idx+1])

        return [lo,hi]
class Solution2:
    # tle
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k=len(nums)
        pointers=[0]*k
        left,right=float('-inf'),float('inf')
        res=float('inf')
        while True:
            if any(pointers[i]==len(nums[i]) for i in range(k)):
                break
            minn = min(nums[i][pointers[i]] for i in range(k))
            maxx = max(nums[i][pointers[i]] for i in range(k))
            minn_i=[i for i in range(k) if nums[i][pointers[i]]==minn][0] # works because every item is unique
            maxx_i=[i for i in range(k) if nums[i][pointers[i]]==maxx][0] # works because every item is unique
            if res>maxx-minn:
                res=maxx-minn
                left=nums[minn_i][pointers[minn_i]]
                right=nums[maxx_i][pointers[maxx_i]]
            pointers[minn_i]+=1
        return [left,right]

class Solution3:
    # tle
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def valid(left, right):
            for li in nums:
                idx1=bisect_left(li, left)
                idx2=bisect_left(li, right)
                if idx2-idx1>=1: continue
                if idx1<len(li) and li[idx1]==left: continue
                if idx2<len(li) and li[idx2]==right: continue
                return False
            return True
        def func(left:int): # given lower bound find smallest upper bound
            # if left>MAXX: return float('inf')
            lo=left
            hi=10**6+1
            while lo<=hi:
                mid=(lo+hi)//2
                if valid(left,mid):
                    hi=mid-1
                else:
                    lo=mid+1
            return lo


        MAXX=max(max(nums,key=lambda x:max(x)))
        MINN=min(min(nums,key=lambda x:min(x)))

        # x=func(100000)
        # print(x)

        lo,hi=float("-inf"),float("inf")
        for left in range(MINN,MAXX):
            right=func(left)
            if right-left<hi-lo:
                lo,hi=left,right
        return [lo,hi]


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        Output= [20,24]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    def test2(self):
        nums = [[1,2,3],[1,2,3],[1,2,3]]
        Output= [1,1]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    def test3(self):
        nums = [[10,10],[11,11]]
        Output= [10,11]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    def test4(self):
        nums = [[10],[11]]
        Output= [10,11]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    def test5(self):
        nums = [[1],[2],[3],[4],[5],[6],[7]]
        Output= [1,7]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    def test6(self):
        nums = [[24992,50748,95744,95883,96215,96220,96228,96261,96262,96282,96283,96298,96300,96301,96302],[-49982,-30856,-18263,7707,14170,14403,16538,16590,16609,16624,16633],[-2278,3082,4526,4584,5656,5774,5789,5818,5819],[3350,52729,52767,52894,53034,53037,53062,53069,53069,53073],[-37125,5045,6966,13789,16629,19193,20841,32593,33460,33561,33583,33750,33770,33774,33775,33776,33777,33782],[2695,13193,22821,33445,34016,35303,35634,35975,35994,36193,36244,36268,36272],[22400,23016,27567,49766,51312,53582,53832,53852,53866,53867,53871,53871,53871,53871,53873],[40102,58020,86502,88062,88626,88645,88645,88650,88650,88651],[8493,57620,58817,60167,60204,60531,60742,60751,60846,60873,60880,60889,60890,60892,60892,60893],[-18345,12083,12184,15480,15503,15527,15537,15542],[-55646,26553,27767,30264,33045,35099,37668,37736,37814,37918,37923,37929,37931,37932],[55460,85320,87101,87138,87290,87402,87432,87467,87485,87504,87504,87504,87505],[47076,47436,47738,63970,70611,78538,79347,79376,79455,79463,79493,79497,79497,79498,79502]]
        Output= [5819, 55460]
        self.assertEqual(Output, get_sol().smallestRange(nums))
    # def test7(self):
    # def test8(self):