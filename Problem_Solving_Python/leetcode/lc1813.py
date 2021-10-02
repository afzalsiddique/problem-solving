import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1,words2 = sentence1.split(), sentence2.split()
        m,n=len(words1),len(words2)
        if m<n: return self.areSentencesSimilar(sentence2,sentence1)
        i1,j1=0,0
        while j1<n and words1[i1]==words2[j1]:
            i1+=1
            j1+=1
        if j1==n: return True
        i2=m-1
        j2=n-1
        while j2>=0 and j2>=j1 and words1[i2]==words2[j2]:
            i2-=1
            j2-=1
        if j2<j1: return True
        return False


class MyTestCase(unittest.TestCase):
    def test_1(self):
        sentence1,sentence2 = "My name is Haley",  "My Haley"
        Output= True
        self.assertEqual(Output, get_sol().areSentencesSimilar(sentence1,sentence2))
    def test_2(self):
        sentence1,sentence2 = "of",  "A lot of words"
        Output= False
        self.assertEqual(Output, get_sol().areSentencesSimilar(sentence1,sentence2))
    def test_3(self):
        sentence1,sentence2 = "Eating right now",  "Eating"
        Output= True
        self.assertEqual(Output, get_sol().areSentencesSimilar(sentence1,sentence2))
    def test_4(self):
        sentence1,sentence2 = "Luky",  "Lucccky"
        Output= False
        self.assertEqual(Output, get_sol().areSentencesSimilar(sentence1,sentence2))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
