from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List




class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_nums(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        n=len(nums)
        k=k%n
        reverse_nums(0,n-k-1)
        reverse_nums(n-k,n-1)
        nums.reverse()
