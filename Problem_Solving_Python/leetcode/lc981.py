import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return TimeMap()
class MyVal:
    def __init__(self):
        self.times = []
        self.values = []
    def add(self,val,time):
        self.times.append(time)
        self.values.append(val)
    def retrive(self, time):
        if not self.times: return ""
        if time<self.times[0]: return ""
        times = self.times
        idx = bisect_right(times,time)
        idx-=1
        return self.values[idx]
    def __repr__(self):
        return "times: {} values: {}".format(self.times, self.values)
class TimeMap:
    def __init__(self):
        self.di = defaultdict(MyVal)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di[key].add(value,timestamp)
    def get(self, key: str, timestamp: int) -> str:
        return self.di[key].retrive(timestamp)


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='TimeMap':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='set':
                outputs.append(obj.set(input[0],input[1],input[2]))
            elif cmd=='get':
                outputs.append(obj.get(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
        inputs=[     [], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
        expected = [None, None,              "bar",      "bar",         None,             "bar2",    "bar2"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["TimeMap",    "set",            "set",          "get",     "get",      "get",        "get",    "get"]
        inputs=[     [],    ["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        expected = [None,        None,             None,            "",       "high",      "high",      "low",   "low"]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["TimeMap",    "set",         "set",      "get",    "set",         "get",   "get"]
        inputs=[      [],        ["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
        expected = [None, None, None, '', None, 'bar2', 'bar2']
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

