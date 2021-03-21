from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Solution:
    def secondHighest(self, s: str) -> int:
        sett = set()
        for c in s:
            if c >='0' and c<='9':
                sett.add(c)
        if len(sett)==1 or len(sett)==0:return -1
        li = list(sett)
        li.sort()
        return li[-2]


print(secondHighest("dfa12321afd"))
print(secondHighest("abc1111"))
