import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(x,y): return CombinationIterator(x,y)
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.indices = [i for i in range(combinationLength)]
        self.indices[-1]-=1
    def next(self) -> str:
        indices = self.indices
        m=self.combinationLength
        n=len(self.characters)
        if indices[m-1]+1<n:
            indices[m-1]+=1
            return self.get_combination()
        for i in range(m-2,-1,-1):
            if indices[i]+(m-i)<n:
                break
        indices[i]+=1
        j=i+1
        for i in range(j,m):
            indices[i]=indices[i-1]+1
        return self.get_combination()

    def hasNext(self) -> bool:
        indices = self.indices
        if len(indices)==1 and indices[-1]==-1: return True
        comb = self.get_combination()
        characters = self.characters
        m=self.combinationLength
        if comb==characters[-m:]:
            return False
        return True

    def get_combination(self):
        indices = self.indices
        chars = self.characters
        res = [chars[indices[i]] for i in range(len(indices))]
        return ''.join(res)
class CombinationIterator2:
    # bad solution. pre calculated
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
        inputs=[["abc", 2], [], [], [], [], [], []]
        expected = [None, "ab", True, "ac", True, "bc", False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["CombinationIterator","hasNext","next","hasNext","hasNext","next","next","hasNext","hasNext","hasNext","hasNext"]
        inputs=[["chp",1],[],[],[],[],[],[],[],[],[],[]]
        expected = [None,True,"c",True,True,"h","p",False,False,False,False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

