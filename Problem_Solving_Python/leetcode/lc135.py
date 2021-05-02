import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
    # https://www.youtube.com/watch?v=h6_lIwZYHQw
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1: return 1
        left,right=[1]*n,[1]*n
        for i in range(n):
            if i>0 and ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        for i in reversed(range(n)):
            if i < n-1 and ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        maxx=[max(left[i],right[i]) for i in range(n)]
        return sum(maxx)
