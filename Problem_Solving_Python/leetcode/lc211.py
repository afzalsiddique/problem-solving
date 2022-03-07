import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        # self.children = {}
        self.end_node = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # if using dict
    # def addWord(self, word):
    #     cur = self.root
    #     for c in word:
    #         if c not in cur.children:
    #             cur.children[c]=TrieNode()
    #         cur=cur.children[c]
    #     cur.end_node = True

    # if using defaultdict
    def addWord(self, word):
        cur = self.root
        for c in word:
            cur=cur.children[c]
        cur.end_node = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1): return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)

            return False

        return dfs(self.root, 0)

class TrieNode2:
    def __init__(self):
        self.children=defaultdict(TrieNode2)
        self.isWord=False
class Trie:
    def __init__(self): self.root=TrieNode2()
    def __repr__(self): return str(self.root.children)
    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            node=node.children[c]
        node.isWord=True
class WordDictionary2:
    def __init__(self):
        self.trie=Trie()
    def addWord(self, word: str) -> None:
        self.trie.insert(word)
    def searchUtil(self,node:TrieNode2,i:int,word:List[str]):
        c=word[i]
        if i==len(word)-1:
            if c=='.': return any(node.children[child].isWord for child in node.children)
            return c in node.children and node.children[c].isWord
        if i==len(word): return True
        if c=='.':
            return any(self.searchUtil(node.children[child],i+1,word) for child in node.children)
        if c not in node.children:
            return False
        return self.searchUtil(node.children[c],i+1,word)
    def search(self, word: str) -> bool:
        node=self.trie.root
        return self.searchUtil(node,0,list(word))
class MyTestCase(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = [None]*len(inputs)
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='WordDictionary': obj = WordDictionary()
            elif cmd=='addWord': obj.addWord(input[0])
            elif cmd=='search': outputs[i] = obj.search(input[0])
        return outputs

    def test01(self):
        commands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        inputs = [        [],         ["bad"],  ["dad"],  ["mad"], ["pad"],  ["bad"], [".ad"],["b.."]]
        expected = [     None,         None,     None,    None,    False,     True,     True,   True]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test02(self):
        commands = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
        inputs = [[],                ["at"],     ["and"], ["an"],  ["add"],   ["a"],  [".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
        expected = [None,            None,       None,   None,      None,     False,   False,None,True,True,False,False,True,False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

