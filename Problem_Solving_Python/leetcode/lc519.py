import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(r,c): return Solution(r,c)
class Solution:
    # memory limit
    def __initialize(self,r,c):
        n=r*c
        indices=[i for i in range(n)]
        i=n
        while i!=1:
            j=random.randrange(i)
            i-=1
            indices[i],indices[j]=indices[j],indices[i]
        self.indices=indices
    def __init__(self, n_rows: int, n_cols: int):
        self.r=n_rows
        self.c=n_cols
        self.__initialize(self.r,self.c)
    def flip(self) -> List[int]:
        idx=self.indices.pop()
        c=self.c
        return [idx//c,idx%c]
    def reset(self) -> None:
        self.__initialize(self.r,self.c)

class Solution2:
    # tle
    def __initialize(self,r,c):
        prob=[]
        idx=[i for i in range(r*c)]
        for _ in range(r*c):
            prob.append(random.random())
        prob,idx=zip(*sorted(zip(prob,idx)))
        self.idx=list(idx)
    def __init__(self, n_rows: int, n_cols: int):
        self.r=n_rows
        self.c=n_cols
        self.__initialize(self.r,self.c)
    def flip(self) -> List[int]:
        idx=self.idx.pop()
        c=self.c
        return [idx//c,idx%c]
    def reset(self) -> None:
        self.__initialize(self.r,self.c)


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Solution':
                obj = get_sol(input[0],input[1])
                outputs.append(None)
            elif cmd=='flip':
                outputs.append(obj.flip())
            elif cmd=='reset':
                outputs.append(obj.reset())
        return outputs
    def test_01(self):
        commands = ["Solution", "flip", "flip", "flip", "reset", "flip"]
        inputs=[[3, 1], [], [], [], [], []]
        expected = [None, [1, 0], [2, 0], [0, 0], None, [2, 0]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)