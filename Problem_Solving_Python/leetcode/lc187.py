import pickle
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# rolling hash
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:








# time O(10*len(DNA)). space O(len(DNA)/10)
class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di=defaultdict(int)
        res=[]
        for i in range(len(s)-10+1):
            di[s[i:i+10]]+=1
        for seq in di:
            if di[seq]>1: res.append(seq)
        return res