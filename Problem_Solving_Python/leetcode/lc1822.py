from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zero =False
        neg = 0
        for num in nums:
            if num==0:
                zero=True
                break
            if num<0:
                neg+=1

        if zero:return 0
        if neg%2==0:return 1
        return -1
