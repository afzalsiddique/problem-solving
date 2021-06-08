import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Trie3()
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58989/My-python-solution
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/493673/python3-array-and-hashTable-Sol
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1093872/Python-Array-Solution-consice

# using array
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            idx = ord(char)-ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return True

# using dict
class TrieNode2:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie2:

    def __init__(self):
        self.root = TrieNode2()


    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode2()
            cur=cur.children[char]
        cur.word=True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.word


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True

# using defaultdict
class TrieNode3:
    def __init__(self):
        self.children = defaultdict(TrieNode3)
        self.word = False

class Trie3:
    def __init__(self):
        self.root=TrieNode3()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            cur=cur.children[c]
        cur.word=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Trie':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='insert':
                outputs.append(obj.insert(input[0]))
            elif cmd=='search':
                outputs.append(obj.search(input[0]))
            elif cmd=='startsWith':
                outputs.append(obj.startsWith(input[0]))
        return outputs
    def test01(self):
        commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        inputs=[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        out_exptected = [None, None, True, False, True, None, True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
