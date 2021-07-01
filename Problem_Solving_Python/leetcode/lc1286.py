import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(characters,combinationLength): return CombinationIterator(characters,combinationLength)
class CombinationIterator:
    # bad solution
    # pre calculated
    def helper(self,start, char_left, path,characters,res):
        if char_left==0:
            res.append(''.join(path))
            return
        for i in range(start+1,len(characters)):
            self.helper(i, char_left - 1, path+[characters[i]],characters,res)
    def __init__(self, characters: str, combinationLength: int):
        self.res=deque()
        self.helper(-1,combinationLength,[],characters,self.res)

    def next(self) -> str:
        return self.res.popleft()

    def hasNext(self) -> bool:
        if self.res: return True
        return False


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='CombinationIterator':
                obj = get_sol(input[0],input[1])
                outputs.append(None)
            elif cmd=='next':
                outputs.append(obj.next())
            elif cmd=='hasNext':
                outputs.append(obj.hasNext())
        return outputs
    def test_01(self):
        commands = ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
        inputs=[         ["abc", 2],        [],       [],       [],      [],        [],     []]
        out_exptected = [None,              "ab",    True,     "ac",    True,      "bc", False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)