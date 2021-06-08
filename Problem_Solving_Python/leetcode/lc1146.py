import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# def get_sol(): return Solution()
class SnapshotArray(object):
    # https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search
    def __init__(self, n):
        self.li = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.li[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect_left(self.li[index], [snap_id + 1]) - 1
        return self.li[index][i][1]

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='SnapshotArray':
                obj = SnapshotArray(input[0])
                outputs.append(None)
            elif cmd=='set':
                outputs.append(obj.set(input[0],input[1]))
            elif cmd=='snap':
                outputs.append(obj.snap())
            elif cmd=='get':
                outputs.append(obj.get(input[0],input[1]))
        return outputs
    def test_1(self):
        commands = ["SnapshotArray","set","snap","set","get"]
        inputs=[         [3],       [0,5],  [],  [0,6],[0,0]]
        out_exptected = [None,None,0,None,5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_2(self):
        commands = ["SnapshotArray","snap","snap","get","set","snap","set"]
        inputs=[[4],[],[],[3,1],[2,4],[],[1,4]]
        out_exptected = [None,0,1,0,None,2,None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_3(self):
        commands = ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
        inputs=[             [1], [0,15],   [],    [],   [],   [0,2], [],     [], [0,0]]
        out_exptected = [    None, None,    0,     1,    2,     15,    3,     4,  15]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_4(self):
        commands = ["SnapshotArray","snap","get","get","set","get","set","get","set"]
        inputs=[          [2],[],[1,0],[0,0],[1,8],[1,0],[0,20],[0,0],[0,7]]
        out_exptected = [None,0,   0,    0,   None,  0,   None,   0,   None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_5(self):
        commands = ["SnapshotArray","set","set","set","snap","set", "set", "get","set"]
        inputs=[         [4],       [0,8],[2,5],[3,2],  [],  [2,20],[0,14],[3,0],[0,9]]
        out_exptected = [None,None,None,None,0,None,None,2,None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)

