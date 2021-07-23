import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bucket sort
    def arrangeWords(self, text: str) -> str:
        def capitalize_first_letter():
            first_word = [res[0][0].upper()] + [res[0][1:]]
            first_word = ''.join(first_word)
            res[0] = first_word

        BIG = 100
        text=text.lower()
        text=text.split()
        buckets=[[] for _ in range(BIG)]
        for i,word in enumerate(text):
            buckets[len(word)].append(i)
        res=[]
        for i in range(BIG):
            for j in range(len(buckets[i])):
                res.append(text[buckets[i][j]])
        capitalize_first_letter()
        return ' '.join(res)
class Solution2:
    def arrangeWords(self, text: str) -> str:
        text=text.lower()
        text=text.split()
        text.sort(key=lambda x: len(x))
        first_word = [text[0][0].upper()] + [text[0][1:]]
        first_word = ''.join(first_word)
        text[0] = first_word
        return ' '.join(text)


class tester(unittest.TestCase):
    def test_1(self):
        text = "Leetcode is cool"
        Output= "Is cool leetcode"
        self.assertEqual(Output,get_sol().arrangeWords(text))
    def test_2(self):
        text = "Keep calm and code on"
        Output= "On and keep calm code"
        self.assertEqual(Output,get_sol().arrangeWords(text))
    def test_3(self):
        text = "To be or not to be"
        Output= "To be or to be not"
        self.assertEqual(Output,get_sol().arrangeWords(text))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
