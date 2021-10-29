import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return Solution(x)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self, head:ListNode ):
        self.li = []
        while head:
            self.li.append(head.val)
            head=head.next

    def getRandom(self) -> int:
        n=len(self.li)
        idx = random.randint(0,n-1)
        return self.li[idx]

class Solution2:
    # reservoire sampling
    def __init__(self, head:ListNode ):
        self.head=head
    def getRandom(self) -> int:
        cur = self.head
        res=-1
        count = 0
        while cur:
            tmp = random.randint(0,count)
            if tmp==0:
                res=cur.val
            count+=1
            cur=cur.next
        return res

