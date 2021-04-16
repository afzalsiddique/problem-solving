import builtins
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List




# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# iterate from the back using stack
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        for i in reversed(nestedList):
            self.stack.append(i)

    def next(self)->int:
        return self.stack.pop().getInteger()

    def hasNext(self)->bool:
        while self.stack:
            currInteger = self.stack[-1]
            if currInteger.isInteger():
                return True
            currInteger= self.stack.pop()
            for i in reversed(currInteger.getList()):
                self.stack.append(i)
        return False

# iterate from the front using queue
class NestedIterator2:

    def __init__(self, nestedList: [NestedInteger2]):
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