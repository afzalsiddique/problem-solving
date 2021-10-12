import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return DetectSquares()
class DetectSquares:
    def __init__(self):
        self.freq = Counter()
    def add(self, point: List[int]) -> None:
        self.freq[(point[0], point[1])]+=1
    def count(self, point: List[int]) -> int:
        #    (x1,y1)                          (x4,y1) -> (x2,y2)
        #
        #
        #    (x1,y4) -> (x3,y3)               (x4,y4)
        freq = self.freq
        res=0
        x1,y1 = point
        for x4,y4 in freq:
            if (x1,y1)==(x4,y4): continue # area 0
            if abs(x1-x4)!=abs(y1-y4): continue # diagonals are not equal. not square.
            x2,y2 = x4,y1
            x3,y3 = x1,y4
            res += freq[x2,y2]*freq[x3,y3]*freq[x4,y4]
        return res
class DetectSquares2:
    def __init__(self):
        self.freq = Counter()
    def add(self, point: List[int]) -> None:
        self.freq[(point[0], point[1])]+=1
    def count(self, point: List[int]) -> int:
        #    (x1,y1)                         (x3,y3)
        #
        #
        #    (x2,y2)                         (x3,y2) = (x4,y4)
        freq = self.freq
        res=0
        x1,y1 = point
        for (x2,y2) in freq:
            if (x2,y2)==(x1,y1): continue # area 0
            if x2!=x1: continue
            for x3,y3 in freq:
                if (x3,y3)==(x2,y2) or (x3,y3)==(x2,y2): continue # area 0
                if y3!=y1: continue
                x4,y4 = (x3,y2)
                if abs(x1-x4) != abs(y1-y4): continue # diagonals are not equal. not square.
                res += freq[x2,y2]*freq[x3,y3]*freq[x4,y4]
        return res

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='DetectSquares':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='add':
                outputs.append(obj.add(input[0]))
            elif cmd=='count':
                outputs.append(obj.count(input[0]))
        return outputs
    def test_01(self):
        commands = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
        inputs=[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
        expected = [None, None, None, None, 1, 0, None, 2]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["DetectSquares","add","add",     "add",  "count","add",   "add",  "add", "count",  "add", "add",  "add", "count","add",   "add",  "add",  "count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count"]
        inputs=[[],              [[5,10]],[[10,5]],[[10,10]],[[5,5]],[[3,0]],[[8,0]],[[8,5]],[[3,5]],[[9,0]],[[9,8]],[[1,8]],[[1,0]],[[0,0]],[[8,0]],[[8,8]],[[0,8]],[[1,9]],[[2,9]],[[2,10]],[[1,10]],[[7,8]],[[2,3]],[[2,8]],[[7,3]],[[9,10]],[[9,5]],[[4,5]],[[4,10]],[[0,9]],[[4,5]],[[4,9]],[[0,5]],[[1,10]],[[10,1]],[[10,10]],[[1,1]],[[10,0]],[[2,0]],[[2,8]],[[10,8]],[[7,6]],[[4,6]],[[4,9]],[[7,9]],[[10,9]],[[10,0]],[[1,0]],[[1,9]],[[0,9]],[[8,1]],[[0,1]],[[8,9]],[[3,9]],[[10,9]],[[3,2]],[[10,2]],[[3,8]],[[9,2]],[[3,2]],[[9,8]],[[0,9]],[[7,9]],[[0,2]],[[7,2]],[[10,1]],[[1,10]],[[10,10]],[[1,1]],[[6,10]],[[2,6]],[[6,6]],[[2,10]],[[6,0]],[[6,2]],[[8,2]],[[8,0]],[[6,5]],[[7,4]],[[6,4]],[[7,5]],[[2,10]],[[8,4]],[[2,4]],[[8,10]],[[2,6]],[[2,5]],[[1,5]],[[1,6]],[[10,9]],[[10,0]],[[1,9]],[[1,0]],[[0,9]],[[5,9]],[[0,4]],[[5,4]],[[3,6]],[[9,0]],[[3,0]],[[9,6]],[[0,2]],[[1,1]],[[0,1]],[[1,2]],[[1,7]],[[8,0]],[[8,7]],[[1,0]],[[2,7]],[[4,5]],[[2,5]],[[4,7]],[[6,7]],[[3,7]],[[6,4]],[[3,4]],[[10,2]],[[2,10]],[[2,2]],[[10,10]],[[10,1]],[[1,10]],[[1,1]],[[10,10]],[[2,10]],[[2,9]],[[3,9]],[[3,10]],[[10,1]],[[1,10]],[[1,1]],[[10,10]],[[10,4]],[[10,3]],[[9,4]],[[9,3]],[[6,6]],[[6,10]],[[10,6]],[[10,10]],[[9,7]],[[4,7]],[[9,2]],[[4,2]],[[2,3]],[[2,1]],[[0,3]],[[0,1]],[[2,8]],[[10,8]],[[2,0]],[[10,0]],[[8,4]],[[2,10]],[[8,10]],[[2,4]],[[0,0]],[[9,9]],[[0,9]],[[9,0]],[[5,7]],[[5,8]],[[4,7]],[[4,8]],[[10,10]],[[10,1]],[[1,1]],[[1,10]],[[6,8]],[[7,8]],[[6,9]],[[7,9]],[[4,6]],[[1,6]],[[4,3]],[[1,3]],[[10,1]],[[1,10]],[[10,10]],[[1,1]],[[7,7]],[[7,10]],[[4,7]],[[4,10]],[[0,0]],[[8,0]],[[0,8]],[[8,8]],[[3,5]],[[2,4]],[[3,4]],[[2,5]],[[0,6]],[[0,2]],[[4,2]],[[4,6]],[[5,2]],[[9,6]],[[9,2]],[[5,6]],[[1,1]],[[1,10]],[[10,10]],[[10,1]],[[7,5]],[[2,0]],[[2,5]],[[7,0]],[[1,9]],[[1,2]],[[8,2]],[[8,9]],[[3,8]],[[3,3]],[[8,3]],[[8,8]],[[3,10]],[[9,10]],[[3,4]],[[9,4]],[[0,2]],[[0,10]],[[8,10]],[[8,2]],[[9,4]],[[8,4]],[[8,5]],[[9,5]],[[9,8]],[[4,3]],[[4,8]],[[9,3]],[[4,9]],[[0,5]],[[0,9]],[[4,5]],[[1,3]],[[3,5]],[[1,5]],[[3,3]],[[0,0]],[[0,8]],[[8,0]],[[8,8]],[[2,8]],[[10,0]],[[10,8]],[[2,0]],[[8,1]],[[0,9]],[[8,9]],[[0,1]],[[4,9]],[[4,6]],[[1,9]],[[1,6]],[[0,9]],[[0,8]],[[1,9]],[[1,8]],[[5,1]],[[5,6]],[[10,1]],[[10,6]],[[9,2]],[[2,2]],[[2,9]],[[9,9]],[[5,5]],[[8,5]],[[5,8]],[[8,8]],[[8,0]],[[1,0]],[[8,7]],[[1,7]],[[8,2]],[[5,5]],[[5,2]],[[8,5]],[[6,6]],[[6,8]],[[8,6]],[[8,8]],[[2,10]],[[10,2]],[[2,2]],[[10,10]],[[1,9]],[[8,2]],[[1,2]],[[8,9]],[[7,4]],[[7,2]],[[9,4]],[[9,2]],[[1,9]],[[1,0]],[[10,0]],[[10,9]],[[2,10]],[[2,3]],[[9,10]],[[9,3]],[[10,0]],[[1,0]],[[1,9]],[[10,9]],[[8,10]],[[1,10]],[[1,3]],[[8,3]],[[0,9]],[[9,9]],[[0,0]],[[9,0]],[[7,9]],[[8,9]],[[7,8]],[[8,8]],[[3,1]],[[9,7]],[[9,1]],[[3,7]],[[5,9]],[[6,9]],[[5,8]],[[6,8]],[[0,1]],[[0,10]],[[9,10]],[[9,1]],[[8,0]],[[8,2]],[[10,2]],[[10,0]],[[8,0]],[[0,8]],[[8,8]],[[0,0]],[[6,7]],[[5,8]],[[5,7]],[[6,8]],[[0,9]],[[0,2]],[[7,9]],[[7,2]],[[5,0]],[[5,5]],[[10,0]],[[10,5]],[[1,10]],[[10,10]],[[10,1]],[[1,1]],[[9,2]],[[9,10]],[[1,2]],[[1,10]],[[1,10]],[[10,1]],[[10,10]],[[1,1]],[[9,9]],[[0,9]],[[0,0]],[[9,0]],[[9,6]],[[9,3]],[[6,3]],[[6,6]],[[10,4]],[[6,0]],[[10,0]],[[6,4]],[[6,8]],[[0,2]],[[0,8]],[[6,2]],[[7,9]],[[0,9]],[[7,2]],[[0,2]],[[9,1]],[[9,10]],[[0,10]],[[0,1]],[[10,0]],[[10,9]],[[1,9]],[[1,0]],[[1,6]],[[1,9]],[[4,9]],[[4,6]],[[0,8]],[[1,9]],[[0,9]],[[1,8]],[[1,1]],[[9,1]],[[1,9]],[[9,9]],[[2,5]],[[2,9]],[[6,5]],[[6,9]],[[7,3]],[[2,3]],[[2,8]],[[7,8]],[[9,4]],[[4,4]],[[9,9]],[[4,9]],[[4,4]],[[2,4]],[[4,2]],[[2,2]],[[0,3]],[[0,2]],[[1,3]],[[1,2]],[[10,9]],[[10,2]],[[3,2]],[[3,9]],[[5,6]],[[10,6]],[[10,1]],[[5,1]],[[9,0]],[[0,9]],[[9,9]],[[0,0]],[[5,6]],[[9,2]],[[9,6]],[[5,2]],[[3,3]],[[10,3]],[[10,10]],[[3,10]],[[2,4]],[[2,10]],[[8,4]],[[8,10]],[[4,9]],[[1,9]],[[4,6]],[[1,6]],[[1,8]],[[9,0]],[[1,0]],[[9,8]],[[10,3]],[[5,8]],[[5,3]],[[10,8]],[[8,2]],[[0,10]],[[8,10]],[[0,2]],[[9,0]],[[2,7]],[[9,7]],[[2,0]],[[0,4]],[[5,9]],[[0,9]],[[5,4]],[[5,3]],[[10,3]],[[5,8]],[[10,8]],[[6,4]],[[7,4]],[[6,5]],[[7,5]],[[9,1]],[[0,1]],[[9,10]],[[0,10]],[[5,10]],[[5,7]],[[8,7]],[[8,10]],[[8,0]],[[8,7]],[[1,7]],[[1,0]],[[1,1]],[[9,9]],[[1,9]],[[9,1]],[[3,1]],[[3,5]],[[7,5]],[[7,1]],[[5,8]],[[5,3]],[[10,8]],[[10,3]],[[0,9]],[[2,7]],[[2,9]],[[0,7]],[[9,3]],[[9,7]],[[5,3]],[[5,7]],[[0,0]],[[9,0]],[[9,9]],[[0,9]],[[6,4]],[[4,2]],[[4,4]],[[6,2]],[[1,9]],[[1,5]],[[5,5]],[[5,9]],[[7,7]],[[0,7]],[[0,0]],[[7,0]],[[1,3]],[[1,9]],[[7,3]],[[7,9]],[[0,9]],[[9,9]],[[9,0]],[[0,0]],[[1,8]],[[3,6]],[[3,8]],[[1,6]]]
        expected = [None,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,2,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,2,None,None,None,2,None,None,None,2,None,None,None,2,None,None,None,5,None,None,None,6,None,None,None,2,None,None,None,3,None,None,None,3,None,None,None,14,None,None,None,3,None,None,None,1,None,None,None,2,None,None,None,2,None,None,None,4,None,None,None,20,None,None,None,4,None,None,None,5,None,None,None,10,None,None,None,26,None,None,None,8,None,None,None,3,None,None,None,7,None,None,None,21,None,None,None,20,None,None,None,52,None,None,None,6,None,None,None,56,None,None,None,2,None,None,None,5,None,None,None,17,None,None,None,18,None,None,None,13,None,None,None,19,None,None,None,102,None,None,None,9,None,None,None,2,None,None,None,157,None,None,None,23,None,None,None,29,None,None,None,23,None,None,None,15,None,None,None,24,None,None,None,186,None,None,None,12,None,None,None,32,None,None,None,36,None,None,None,10,None,None,None,35,None,None,None,20,None,None,None,43,None,None,None,48,None,None,None,35,None,None,None,73,None,None,None,59,None,None,None,56,None,None,None,72,None,None,None,198,None,None,None,37,None,None,None,145,None,None,None,130,None,None,None,45,None,None,None,68,None,None,None,172,None,None,None,281,None,None,None,147,None,None,None,53,None,None,None,160,None,None,None,105,None,None,None,253,None,None,None,82,None,None,None,103,None,None,None,248,None,None,None,75,None,None,None,86,None,None,None,312,None,None,None,301,None,None,None,273,None,None,None,119,None,None,None,191,None,None,None,61,None,None,None,584,None,None,None,696,None,None,None,802,None,None,None,293,None,None,None,104,None,None,None,114,None,None,None,242,None,None,None,259,None,None,None,300,None,None,None,465,None,None,None,180,None,None,None,1082,None,None,None,697,None,None,None,187,None,None,None,113,None,None,None,201,None,None,None,520,None,None,None,652,None,None,None,197,None,None,None,91,None,None,None,670,None,None,None,159,None,None,None,189,None,None,None,386,None,None,None,403,None,None,None,204,None,None,None,301,None,None,None,378,None,None,None,314,None,None,None,292,None,None,None,352,None,None,None,174,None,None,None,2778,None,None,None,473,None,None,None,869,None,None,None,1568,None,None,None,190,None,None,None,198,None,None,None,342,None,None,None,286,None,None,None,1062,None,None,None,475,None,None,None,354,None,None,None,174,None,None,None,574,None,None,None,1605,None,None,None,547]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
