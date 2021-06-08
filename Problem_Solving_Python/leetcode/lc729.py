import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# def get_sol(): return Solution()
class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
    def __repr__(self): return '(' +str(self.s) + ',' + str(self.e) +')'

    def insert(self, start, end):
        if self.s >= end:
            if self.left is None:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:
            if self.right is None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False


class MyCalendar(object):

    def __init__(self):
        self.root = None


    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MyCalendar':
                obj = MyCalendar()
                outputs.append(None)
            elif cmd=='book':
                outputs.append(obj.book(input[0],input[1]))
        return outputs
    def test_1(self):
        commands = ["MyCalendar","book","book",  "book"]
        inputs=[        [],     [10,20],[15,25],[20,30]]
        out_exptected = [None,True,False,True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)

