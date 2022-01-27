import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def turnOn(mask,i): return mask|(1<<i)
        def turnOff(mask,i): return mask-(1<<i)
        def isOn(mask,i): return (mask>>i)&1
        def createMask(word):
            mask=0
            for c in word:
                mask=turnOn(mask,ord(c)-ord('a'))
            return mask

        sett=set()
        for w in startWords:
            sett.add(createMask(w))

        res=0
        for word in targetWords:
            mask=createMask(word)
            flag=False
            for c in string.ascii_lowercase:
                idx=ord(c)-ord('a')
                if isOn(mask,idx):
                    newMask=turnOff(mask,idx)
                    if newMask in sett:
                        flag=True
                        break
            res+=flag
        return res
class Solution2:
    # tle
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def makeKey(count:Counter):
            li=[]
            for c in sorted(count.keys()):
                if count[c]==0: continue
                li.append(c+':'+str(count[c]))
            return ' '.join(li)
        def makeKeyOneLess(count:Counter, c:str):
            count[c]-=1
            res=makeKey(count)
            count[c]+=1
            return res
        def valid(count:Counter):
            for c in string.ascii_lowercase:
                if makeKeyOneLess(count,c) in sett:
                    return True
            return False

        sett=set()
        for start in startWords:
            sett.add(makeKey(Counter(start)))

        res=0
        for tar in targetWords:
            if valid(Counter(tar)):
                res+=1
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().wordCount(["ant","act","tack"], ["tack","act","acti"]))
    def test2(self):
        self.assertEqual(1, get_sol().wordCount(["ab","a"], ["abc","abcd"]))
    def test3(self):
        self.assertEqual(0, get_sol().wordCount(["f"], ["g"]))
    def test4(self):
        self.assertEqual(4, get_sol().wordCount(["obmcx","r","bqxc","f","tijlu","mpbk","vxh","ue","x","rb"], ["kf","sxqbc","rq","z","j","rft","oxcbms","g","rdnq","qmc","nzbq"]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
