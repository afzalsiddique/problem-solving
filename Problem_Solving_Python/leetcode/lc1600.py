import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(x): return ThroneInheritance(x)
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = kingName
        self.dead = set()
        self.children = defaultdict(list)
        self.parent = {}
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.parent[childName] = parentName
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        li = []
        def dfs(x):
            if not x: return
            if x not in self.dead:
                li.append(x)
            for c in self.children[x]:
                dfs(c)
        dfs(self.root)
        return li



class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='ThroneInheritance':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='birth':
                outputs.append(obj.birth(input[0],input[1]))
            elif cmd=='death':
                outputs.append(obj.death(input[0]))
            elif cmd=='getInheritanceOrder':
                outputs.append(obj.getInheritanceOrder())
        return outputs
    def test_01(self):
        commands = ["ThroneInheritance", "birth",            "birth",            "birth",           "birth",              "birth",        "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
        inputs=[         ["king"],    ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [None],            ["bob"], [None]]
        expected = [None, None, None, None, None, None, None, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], None, ["king", "andy", "matthew", "alex", "asha", "catherine"]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
