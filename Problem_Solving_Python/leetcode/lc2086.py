import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1= Counter(words1)
        count2= Counter(words2)
        words = set(words1).union(set(words2))
        res=0
        for word in words:
            if count1[word]==1 and count2[word]==1:
                res+=1
        return res

