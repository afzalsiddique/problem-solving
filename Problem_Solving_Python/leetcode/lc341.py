from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(x): return NestedIterator(x)
class NestedInteger:
    def isInteger(self) -> bool:
        pass
    def getInteger(self) -> int:
        pass
    def getList(self):
        pass

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st=[]
        self.prepareStack(nestedList)
    def next(self) -> int:
        if self.hasNext():
            return self.st.pop().getInteger()
    def hasNext(self) -> bool:
        st=self.st
        while st and not st[-1].isInteger():
            li=st.pop().getList()
            self.prepareStack(li)
        return len(st)>0
    def prepareStack(self,li):
        for i in range(len(li)-1,-1,-1):
            self.st.append(li[i])

# iterate from the front using queue
class NestedIterator2:

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque(nestedList)

    def next(self)->int:
        return self.queue.popleft().getInteger()

    def hasNext(self)->bool:
        while self.queue:
            if self.queue[0].isInteger():
                return True
            first = self.queue.popleft()
            self.queue.extendleft(first.getList()[::-1])
        return False