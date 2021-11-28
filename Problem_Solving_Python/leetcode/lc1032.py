import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(x): return StreamChecker(x)
class Node:
    def __init__(self):
        self.is_word=False
        self.children=defaultdict(Node)
    def __repr__(self):
        return str(self.children)
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            cur=cur.children[c]
        cur.is_word=True
    def search(self, word: List[str]) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children: return False
            cur=cur.children[c]
            if cur.is_word: return True # THIS LINE ADDED EXTRA from the trie template
        return cur.is_word

class StreamChecker:
    # add words in reverse order
    # search word in reverse order
    def __init__(self, words: List[str]):
        self.trie=Trie()
        self.maxx=len(max(words,key=lambda x:len(x)))
        for word in words:
            self.trie.insert(word[::-1])
        self.li=[]
    def query(self, letter: str) -> bool:
        self.li.append(letter)
        # select last self.maxx no of letters and reverse it
        x=self.li[-self.maxx:]
        x=list(reversed(x))
        return self.trie.search(x)



class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='StreamChecker':
                obj = get_sol(input[0])
                outputs.append(None)
            elif cmd=='query':
                outputs.append(obj.query(input[0]))
        return outputs
    def test01(self):
        commands = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
        inputs=[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
        out_exptected = [None, False, False, False, True, False, True, False, False, False, False, False, True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
