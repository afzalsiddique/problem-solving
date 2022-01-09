import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def f(word:str):
            if len(word)<=2:
                return word.lower()
            return word[0:1].upper() + word[1:].lower()

        res=list(map(f,title.split()))
        return ' '.join(res)

