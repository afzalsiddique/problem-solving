from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st,n = [],len(T)
        nxt = [0] * n
        for i in range(n):
            while st and T[st[-1]]<T[i]:
                top = st.pop()
                nxt[top] = i-top
            st.append(i)
        return nxt