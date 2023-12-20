import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List

class MaxHeap5(list):
    # simplest max heap
    def __init__(self): super().__init__()
    def heappop(self): return heappop(self)[0]*(-1)
    def push(self,a,b): heappush(self,[-a,-b])
class Heap5(list):
    # both min and max heap with list
    def __init__(self,isMaxHeap=False):
        super().__init__()
        self.mul=-1 if isMaxHeap else 1
    def top(self):
        li=self[0]
        return [x*self.mul for x in li]
    def push(self, li):
        heappush(self, [x*self.mul for x in li])
    def heappop(self):
        li=heappop(self)
        return [x*self.mul for x in li]
class Heap4(list):
    # both min and max heap and two elements
    def __init__(self,isMaxHeap=False):
        super().__init__()
        self.mul=-1 if isMaxHeap else 1
    def topVal(self): return self[0][0]*self.mul
    def topIdx(self): return self[0][1]*self.mul
    def setTopVal(self,val): self[0][0]=val*self.mul
    def setTopIdx(self,val): self[0][1]=val*self.mul
    def push(self, val, idx): heappush(self, [val*self.mul, idx*self.mul])
    def heappop(self):
        tmp=heappop(self)
        return [tmp[0]*self.mul, tmp[1]*self.mul]
# implementation 1.3
class MaxHeap3(list):
    # two elements
    def __init__(self):
        super().__init__()
    def topPrice(self): return -self[0][0]
    def topAmount(self): return -self[0][1]
    def setTopPrice(self,val): self[0][0]=val*(-1)
    def setTopAmount(self,val): self[0][1]=val*(-1)
    def push(self, price, amount): heappush(self, [-price, -amount])
    def heappop(self): return heappop(self)

# implementation 1.2  with two elements
class MaxHeap2(list): # I think we don't need to inherit list class
    def __init__(self):
        super().__init__()
        self.data = []
    def top(self): return -self.data[0]
    def topPrice(self): return -self.data[0][0]
    def topAmount(self): return -self.data[0][1]
    def setTopPrice(self,val): self.data[0][0]=val*(-1)
    def setTopAmount(self,val): self.data[0][1]=val*(-1)
    def push(self, price, amount): heappush(self.data, [-price, -amount])
    def heappop(self):
        val1,val2=heappop(self.data)
        return [-val1,-val2]
    def __repr__(self): return str(self.data)
    def __len__(self): return len(self.data)
    def __bool__(self): return True if len(self.data) else False

# implementation 1.1
class MaxHeap4(list):
    # one element
    def __init__(self): super().__init__()
    def top(self): return -self[0]
    def push(self, val): heappush(self, -val)
    def heappop(self): return -heappop(self)

# implementation 2
class MaxHeap:
    # one element
    def __init__(self):
        self.data = []
    def top(self):
        return -self.data[0]
    def push(self, val):
        heappush(self.data, -val)
    def pop(self):
        return heappop(self.data)*(-1)
    def __repr__(self):
        return str(self.data)

# implementation 3
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
