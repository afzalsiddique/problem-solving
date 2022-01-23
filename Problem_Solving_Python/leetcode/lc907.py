import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=9-TXIVEXX2w
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        st=[]
        next_smaller=[i for i in reversed(range(1,n+1))] # no of elements in the right before the next smaller num appears
        pre_smaller=[i for i in range(1,n+1)] # no of elements in the left before the next smaller num appears
        for i in range(n):
            while st and arr[st[-1]]>arr[i]: # '>' sign used here -> https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/JavaC++Python-Stack-Solution/221762
                top=st.pop()
                next_smaller[top]=i-top
            st.append(i)
        st=[]
        for i in reversed(range(n)):
            while st and arr[st[-1]]>=arr[i]: # '>=' sign used here.
                top=st.pop()
                pre_smaller[top]=top-i
            st.append(i)

        # print("right",next_smaller)
        # print("left",pre_smaller)
        summ=0
        MOD=10**9+7
        for i in range(n):
            summ+=(arr[i]*(pre_smaller[i])*(next_smaller[i]))
            summ%=MOD
        return summ
class Solution2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        nxtSmaller=[n]*n
        st=[]
        for i in range(n):
            while st and arr[i]<arr[st[-1]]:
                top=st.pop()
                nxtSmaller[top]=i
            st.append(i)
        nxtSmaller=[nxtSmaller[i]-i for i in range(n)]

        prevSmaller=[-1]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[i]<=arr[st[-1]]:
                top=st.pop()
                prevSmaller[top]=i
            st.append(i)
        prevSmaller=[i-prevSmaller[i] for i in range(n)]

        res=0
        for i in range(n):
            res+=arr[i]*prevSmaller[i]*nxtSmaller[i]
            res%=(10**9+7)
        return res
class Solution3:
    # tle
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]: # this method is same as 239
        q = deque()
        for i in range(k-1):
            while q and q[-1][1]>nums[i]:
                q.pop()
            q.append((i,nums[i])) # idx, value

        res=[]
        for i in range(k-1,len(nums)):
            while q and q[0][0]<=i-k:
                q.popleft()
            while q and q[-1][1]>nums[i]:
                q.pop()
            q.append((i,nums[i])) # idx, value
            res.append(q[0][1])
        return res
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        summ = 0
        for window_size in range(1,len(arr)+1):
            tmp = self.minSlidingWindow(arr,window_size)
            summ+= sum(tmp)
            summ%=MOD
        return summ

class Solution4:
    # tle
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        summ=0
        summ+=sum(arr)
        summ%=MOD
        for i in range(len(arr)):
            tmp_arr = self.helper(arr)
            # print(tmp_arr)
            summ+=sum(tmp_arr)
            summ%=MOD
            arr=tmp_arr
        return summ

    def helper(self,arr:List[int]):
        res = []
        for i in range(len(arr)-1):
            res.append(min(arr[i],arr[i+1]))
        return res
class MyTestCase(unittest.TestCase):
    def test_01(self):
        arr = [3,1,2,4]
        Output= 17
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    def test_02(self):
        arr = [11,81,94,43,3]
        Output= 444
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    def test_03(self):
        arr = [1,2,3,4,5]
        Output= 35
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    def test_04(self):
        arr = [6,7,8,2,5,4]
        Output= 77
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    def test_05(self):
        arr = [71,55,82,55]
        Output= 593
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    def test06(self):
        arr = [2,1,3,1]
        Output= 13
        self.assertEqual(Output,get_sol().sumSubarrayMins(arr))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
