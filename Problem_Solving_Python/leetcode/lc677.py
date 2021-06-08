import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return MapSum()
class TrieNode:
    def __init__(self,letter):
        self.children = {}
        self.word_count = 0
        self.letter=letter
    def __repr__(self): return "({},{})".format(self.letter,self.word_count)
    # def __repr__(self): return "({},{})".format(self.children,self.word_count)

class MapSum: # Trie
    def __init__(self):
        self.root = TrieNode("#")

    def print_func(self):
        print("printing Trie")
        q = deque([self.root])
        while q:
            s = ""
            for _ in range(len(q)):
                cur = q.popleft()
                s += cur.letter + "->" + str(cur.word_count) + " "
                for child in cur.children:
                    q.append(cur.children[child])
            print(s)
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c]=TrieNode(c)
            cur = cur.children[c]
        cur.word_count=val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return 0
            cur = cur.children[c]
        # self.print_func()
        ans = self.__dfs(cur)
        return ans

    def __dfs(self,cur:TrieNode):
        ans = cur.word_count
        for child in cur.children:
            node = cur.children[child]
            ans+=self.__dfs(node)
        return ans

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MapSum':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='insert':
                outputs.append(obj.insert(input[0],input[1]))
            elif cmd=='sum':
                outputs.append(obj.sum(input[0]))
        return outputs
    def test01(self):
        commands = ["MapSum", "insert", "sum", "insert", "sum"]
        inputs=[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
        out_exptected = [None, None, 3, None, 5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test02(self):
        commands = ["MapSum", "insert",   "sum",   "insert",   "insert",   "sum"]
        inputs=[       [],   ["apple",3], ["ap"], ["app",2], ["apple", 2], ["ap"]]
        out_exptected = [None,None,3,None,None,4]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test03(self):
        commands = ["MapSum", "insert", "sum", "insert", "sum"]
        inputs=[        [],     ["ac",3], ["a"], ["ab",2], ["a"]]
        out_exptected = [None,    None,     3,     None,    5]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)


