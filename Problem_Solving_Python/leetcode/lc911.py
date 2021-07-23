import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(p,t): return TopVotedCandidate(p,t)

class TopVotedCandidate:
    # https://leetcode.com/problems/online-election/discuss/173382/C%2B%2BJavaPython-Binary-Search-in-Times
    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        di=defaultdict(int)
        leader=0
        res=[]
        for i in range(len(persons)):
            p=persons[i]
            di[p]+=1
            if di[p]>=di[leader]:
                leader=p
            res.append(leader)
        # print(res)
        self.res=res
    def q(self, t: int) -> int:
        times=self.times
        idx=bisect_left(times,t)
        if idx==len(times):
            idx-=1
        elif times[idx]!=t:
            idx-=1
        return self.res[idx]


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='TopVotedCandidate':
                obj = get_sol(input[0],input[1])
                outputs.append(None)
            elif cmd=='q':
                outputs.append(obj.q(input[0]))
        return outputs
    def test_01(self):
        commands = ["TopVotedCandidate",               "q","q",  "q","q",  "q","q"]
        inputs=[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
        exptected = [None,                             0,   1,   1,   0,   0,  1]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test_02(self):
        commands = ["TopVotedCandidate",      "q","q",  "q","q",  "q","q",  "q","q",  "q","q"]
        inputs=[[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
        exptected = [None,0,0,0,0,0,0,0,0,0,0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)

