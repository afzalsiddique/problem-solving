from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(x): return PeekingIterator(x)
class Iterator:
    def __init__(self, nums:List[int]):
        self.nums=nums
        self.i=0
    def hasNext(self)->bool:
        return self.i<len(self.nums)
    def next(self)->int:
        res=self.nums[self.i]
        self.i+=1
        return res
class PeekingIterator:
    def __init__(self, iterator:Iterator):
        self.iterator=iterator
        self.q=deque()
    def peek(self):
        q,iterator= self.q, self.iterator
        if not q:
            if iterator.hasNext():
                q.append(iterator.next())
        if q:
            return q[0]
        return -1
    def next(self):
        if self.q: return self.q.popleft()
        return self.iterator.next()
    def hasNext(self):
        return len(self.q)>0 or self.iterator.hasNext()



class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='PeekingIterator': obj = get_sol(Iterator(input[0])); outputs.append(None)
            elif cmd=='hasNext': outputs.append(obj.hasNext())
            elif cmd=='peek': outputs.append(obj.peek())
            elif cmd=='next': outputs.append(obj.next())
        return outputs
    def test01(self):
        commands = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
        inputs=[[[1, 2, 3]], [], [], [], [], []]
        expected = [None, 1, 2, 2, 3, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["PeekingIterator","hasNext","peek","peek","next","next","peek","peek","next","hasNext","peek","hasNext","next","hasNext"]
        inputs=[[[1,2,3,4]],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        expected = [None,True,1,1,1,2,3,3,3,True,4,True,4,False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
