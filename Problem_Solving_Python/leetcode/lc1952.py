import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def isThree(self, n: int) -> bool:
        cnt=0
        sett=set()
        for i in range(1,n+1):
            if cnt>3: break
            if n%i==0:
                sett.add(i)
                cnt+=1
        return cnt==3
