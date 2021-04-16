from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split()
        new_li=[]
        if k>len(s):
            k=len(s)
        for i in range(k):
            new_li.append(li[i])
        return " ".join(new_li)
