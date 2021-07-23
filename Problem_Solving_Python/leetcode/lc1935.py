import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        n=len(text)
        arr=[set() for _ in range(n)]
        for i,word in enumerate(text):
            for ch in word:
                arr[i].add(ch)
        brokenLetters=set(brokenLetters)
        cnt=0
        for i,word in enumerate(text):
            flag=True
            for letter in brokenLetters:
                if letter in arr[i]:
                    flag=False
                    break
            if flag:
                cnt+=1
        return cnt

