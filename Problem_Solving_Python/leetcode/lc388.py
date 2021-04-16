from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def countBits(self, num: int) -> List[int]:
        def divide(num):
            if num==0:return 0,0
            cnt = 0
            temp = num
            while temp!=1:
                temp=temp//2
                cnt+=1
            while cnt:
                temp = temp*2
                cnt-=1
            return temp, num-temp

        def init_dp_array(num):
            dp = [0] * (num + 1)
            i=1
            while i<=num:
                dp[i]=1
                i*=2
            return dp

        dp = init_dp_array(num)
        for i in range(num+1):
            idx1,idx2 = divide(i)
            dp[i] = dp[idx1]+dp[idx2]
        return dp