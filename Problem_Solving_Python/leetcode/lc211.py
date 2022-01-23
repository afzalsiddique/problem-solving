import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class TrieNode:
    def __init__(self):
        # self.children = defaultdict(TrieNode)
        self.children = {}
        self.end_node = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end_node = True

    # if using defaultdict
    # def addWord(self, word):
    #     cur = self.root
    #     for c in word:
    #         cur=cur.children[c]
    #     cur.end_node = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.end_node

            if word[i] == ".":
                for child in node.child:
                    if dfs(node.child[child], i + 1): return True

            if word[i] in node.child:
                return dfs(node.child[word[i]], i + 1)

            return False

        return dfs(self.root, 0)

class MyTestCase(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = [None]*len(inputs)
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='WordDictionary':
                obj = WordDictionary()
            elif cmd=='addWord':
                obj.addWord(input[0])
            elif cmd=='search':
                outputs[i] = obj.search(input[0])
        return outputs
    def test_1(self):
        commands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        inputs = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        outputs = self.do_test(commands, inputs)
        expected = [None,None,None,None,False,True,True,True]
        self.assertEqual(expected,outputs)
