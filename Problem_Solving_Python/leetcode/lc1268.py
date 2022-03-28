from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # trie + dfs
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def dfs(node:Node,path):
            if not node: return
            if len(temp)>=3: return
            if node.is_word: temp.append(''.join(path)+node.val)
            for child in sorted(node.children.keys()):
                path.append(node.val)
                dfs(node.children[child],path)
                path.pop()
        res=[]
        trie = Trie()
        for word in products:
            trie.add(word)

        for i,c in enumerate(searchWord):
            temp=[]
            pre = searchWord[:i+1]
            node,path =trie.startsWith(pre,[])
            if not node:
                res.append([])
                continue
            path.pop()
            dfs(node,path)
            res.append(temp)
        return res


class Node:
    def __init__(self,val):
        self.is_word=False
        self.children={}
        self.val=val
    def __repr__(self): return str(self.val)

class Trie:
    def __init__(self):
        self.root=Node('#')

    def add(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=Node(c)
            node=node.children[c]
        node.is_word=True

    def startsWith(self, prefix: str,path):
        node=self.root
        for c in prefix:
            if c not in node.children: return None,[]
            path.append(c)
            node=node.children[c]
        return node,path

class tester(unittest.TestCase):
    def test01(self):
        products = ["mobile","mouse","moneypot","monitor","mousepad"]
        searchWord = "mouse"
        Output= [ ["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"] ]
        self.assertEqual(Output,get_sol().suggestedProducts(products,searchWord))
    def test02(self):
        products = ["havana"]
        searchWord = "havana"
        Output= [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        self.assertEqual(Output,get_sol().suggestedProducts(products,searchWord))
    def test03(self):
        products = ["bags","baggage","banner","box","cloths"]
        searchWord = "bags"
        Output= [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        self.assertEqual(Output,get_sol().suggestedProducts(products,searchWord))
    def test04(self):
        products = ["havana"]
        searchWord = "tatiana"
        Output= [[],[],[],[],[],[],[]]
        self.assertEqual(Output,get_sol().suggestedProducts(products,searchWord))
