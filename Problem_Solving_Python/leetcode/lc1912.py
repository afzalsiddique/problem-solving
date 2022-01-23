from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList,SortedDict,SortedSet
# from ..template.binary_tree import deserialize,serialize
def get_sol(x,y): return MovieRentingSystem(x,y)
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.maindb={} # di[shop,movie]=price
        self.searchdb=defaultdict(SortedList) # di[movie]=SortedList([price,movie]) # this could be replaced by TreeSet in Java
        self.reportdb=SortedList() # SortedList([price,shop,movie])
        for s,m,p in entries:
            self.maindb[s,m]=p
            self.searchdb[m].add([p,s])
    def search(self, movie: int) -> List[int]:
        return [x[1] for x in self.searchdb[movie][:5]]
    def rent(self, shop: int, movie: int) -> None:
        price=self.maindb[shop,movie]
        self.searchdb[movie].remove([price,shop])
        self.reportdb.add([price,shop,movie])
    def drop(self, shop: int, movie: int) -> None:
        price=self.maindb[shop,movie]
        self.reportdb.remove([price,shop,movie])
        self.searchdb[movie].add([price,shop])
    def report(self) -> List[List[int]]:
        return [[x[1],x[2]] for x in self.reportdb[:5]]


class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            print(i)
            if cmd=='MovieRentingSystem': obj = get_sol(input[0],input[1]); outputs.append(None)
            elif cmd=='search': outputs.append(obj.search(input[0]))
            elif cmd=='rent': outputs.append(obj.rent(input[0],input[1]))
            elif cmd=='drop': outputs.append(obj.drop(input[0],input[1]))
            else: outputs.append(obj.report())
        return outputs
    def test_01(self):
        commands = ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
        inputs=[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
        expected = [None, [1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
        inputs=[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
        expected = [None, [1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
