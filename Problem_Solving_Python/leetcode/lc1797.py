import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(t): return AuthenticationManager(t)
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl=timeToLive
        self.di = OrderedDict()
    def _evict(self,currentTime): # remove all outdated tokens
        to_be_deleted=0
        for x in self.di:
            if self.di[x]<=currentTime:
                to_be_deleted+=1
            else:
                break
        for _ in range(to_be_deleted):
            self.di.popitem(last=False)

        # same logic but concise code
        # while self._dict and next(iter(self._dict.values())) <= currentTime:
        #     self._dict.popitem(last=False)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId not in self.di: # only generate if previously  not generated
            self.di[tokenId] = currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId in self.di: # only renew if already generated
            self.di.move_to_end(tokenId)
            self.di[tokenId]=currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._evict(currentTime)
        return len(self.di)

class AuthenticationManager2:
    # very bad solution
    def __init__(self, timeToLive: int):
        self.ttl=timeToLive
        self.di = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.di:
            self.di[tokenId] = currentTime+self.ttl
        return None

    def renew(self, tokenId: str, currentTime: int) -> None:
        di = self.di
        if tokenId in di and currentTime<di[tokenId]:
            di[tokenId] = currentTime + self.ttl
        return None

    def countUnexpiredTokens(self, currentTime: int) -> int:
        to_be_removed = []
        for tokenId in self.di:
            if self.di[tokenId] <= currentTime:
                to_be_removed.append(tokenId)
        for tokenId in to_be_removed:
            self.di.pop(tokenId)
        return len(self.di)

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='AuthenticationManager':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='generate':
                outputs.append(obj.generate(input[0],input[1]))
            elif cmd=='renew':
                outputs.append(obj.renew(input[0],input[1]))
            elif cmd=='countUnexpiredTokens':
                outputs.append(obj.countUnexpiredTokens(input[0]))
        return outputs
    def test_01(self):
        commands = ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate",   "renew",    "renew", "countUnexpiredTokens"]
        inputs=[          [5],             ["aaa", 1], ["aaa", 2],        [6],            ["bbb", 7],  ["aaa", 8], ["bbb", 10],     [15]]
        expected = [None, None, None, 1, None, None, None, 0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["AuthenticationManager","renew","countUnexpiredTokens","countUnexpiredTokens","generate","generate","renew",    "generate","generate","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate","countUnexpiredTokens","renew"]
        inputs=[            [13],       ["ajvy",1],       [3],                [4],              ["fuzxq",5],["izmry",7],["puv",12],["ybiqb",13],["gm",14],     [15],               [18],                    [19],             ["ybiqb",21],    [23],             [25],                  [26],            ["aqdm",28],        [29],         ["puv",30]]
        expected = [        None,        None,            0,                   0,                   None,       None,     None,      None,         None,       4,                    3,                      3,                 None,            2,               2,                      2,                None,             2,            None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

