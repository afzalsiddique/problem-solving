import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class StockSpanner:
    def __init__(self):
        self.st=[(-1,float('inf'))] # (index,val)
        self.i=0

    def next(self, price: int) -> int:
        st=self.st
        while st and price>=st[-1][1]:
            st.pop()
        ans=self.i-st[-1][0]
        st.append((self.i,price))
        self.i+=1
        return ans

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='StockSpanner':
                obj = StockSpanner()
                outputs.append(None)
            elif cmd=='next':
                outputs.append(obj.next(input[0]))
        return outputs
    def test_1(self):
        commands = ["StockSpanner","next","next","next","next","next","next","next"]
        inputs=[[],[100],[80],[60],[70],[60],[75],[85]]
        out_exptected = [None,1,1,1,2,1,4,6]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)

