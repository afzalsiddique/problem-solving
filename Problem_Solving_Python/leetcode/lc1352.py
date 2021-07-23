import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return ProductOfNumbers()
class ProductOfNumbers:
    def __init__(self):
        self.li=[1]
    def add(self, num: int) -> None:
        if num==0:
            self.li=[1] # remove all elements and reinitialize
        else:
            self.li.append(self.li[-1]*num)
    def getProduct(self, k: int) -> int:
        if k>=len(self.li):
            return 0
        return self.li[-1]//self.li[-k-1]
class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='ProductOfNumbers':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='add':
                outputs.append(obj.add(input[0]))
            elif cmd=='getProduct':
                outputs.append(obj.getProduct(input[0]))
        return outputs
    def test_01(self):
        commands = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
        inputs=[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
        exptected = [None,None,None,None,None,None,20,40,0,None,32]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test_02(self):
        commands = ["ProductOfNumbers","add","add","add","getProduct"]
        inputs=[[],[3],[4],[2],[2]]
        exptected = [None,None,None,None,8]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)
    def test_03(self):
        commands = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct"]
        inputs=[            [],         [2],  [3],  [0],  [4],  [5],    [2],           [3],      [4]]
        exptected = [None,            None,   None,  None, None,None,   20,            0,         0]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(exptected,outputs)






