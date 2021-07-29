import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List

# implementation 1
class Max_heap:
    def __init__(self):
        self.data = []
    def top(self):
        return -self.data[0]
    def push(self, val):
        heappush(self.data, -val)
    def pop(self):
        return heappop(self.data)
    def __repr__(self):
        return str(self.data)

# implementation 2
class MinHeap(object):
    def __init__(self): self.h = []
    def push(self, x): heappush(self.h, x)
    def pop(self): return heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)

class MaxHeap(MinHeap):
    def push(self, x): heappush(self.h, MaxHeapObj(x))
    def pop(self): return heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val
