import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# TLE
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n=len(nums)
        sett=set(nums)
        
        # if all are unique
        if t==0 and len(sett)==n: return False

        for i in range(n):
            for j in range(i+1,i+1+k):
                if j>=n: break
                if abs(nums[i]-nums[j])<=t:
                    return True
        return False
