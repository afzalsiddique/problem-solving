import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(x): return LockingTree(x)
class LockingTree:
    def __init__(self, parent: List[int]):
        n=len(parent)
        self.parent = parent
        self.locks = [-1]*n
        self.children = defaultdict(list)
        for child, par in enumerate(parent):
            self.children[par].append(child)
        self.children.pop(-1)
    def lock(self, num: int, user: int) -> bool:
        if self.locks[num]!=-1: return False
        self.locks[num]=user
        return True
    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num]==-1: return False
        if self.locks[num]!=user: return False
        self.locks[num]=-1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        children = self.children
        def dfs_unlock(num):
            self.locks[num]=-1
            for x in children[num]:
                dfs_unlock(x)

        if self.locks[num]!=-1: return False
        if not self.if_no_locked_ancestor(num): return False
        if not self.if_at_least_one_locked_descendant(num): return False
        dfs_unlock(num)
        self.lock(num,user)
        return True
    def if_at_least_one_locked_descendant(self, num): # at least one locked descendant
        def dfs(node):
            if self.locks[node]!=-1: return True
            for child in self.children[node]:
                if dfs(child): return True
            return False

        return dfs(num)
    def if_no_locked_ancestor(self, num): # can't have any locked ancestor
        node = num
        while node!=0:
            node=self.parent[node]
            if self.locks[node]!=-1: return False
        return True


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='LockingTree':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='lock':
                outputs.append(obj.lock(input[0],input[1]))
            elif cmd=='unlock':
                outputs.append(obj.unlock(input[0],input[1]))
            elif cmd=='upgrade':
                outputs.append(obj.upgrade(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
        inputs=[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
        expected = [None, True, False, True, True, True, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

