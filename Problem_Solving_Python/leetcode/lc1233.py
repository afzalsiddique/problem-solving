import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409075/Standard-Python-Trie-solution-(similar-problems-listed)
    class TrieNode:
        def __init__(self):
            self.children=defaultdict(Solution.TrieNode)
            self.is_end=False
    class Trie:
        def __init__(self):
            self.root=Solution.TrieNode()
        def insert(self,fold):
            node=self.root
            for x in fold:
                node=node.children[x]
            node.is_end=True
        def find(self):
            def dfs(node:Solution.TrieNode,path):
                if node.is_end:
                    res.append('/'+'/'.join(path))
                    return
                for child in node.children:
                    dfs(node.children[child], path + [child])
            res=[]
            dfs(self.root,[])
            return res
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Solution.Trie()
        for fold in folder:
            fold = fold.split('/')[1:]
            trie.insert(fold)
        return trie.find()

class Solution2:
    # https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        for f in sorted(folder):
            if not ans or not f.startswith(ans[-1] + '/'):	#  need '/' to ensure a parent.
                ans.append(f)
        return ans
class Solution3:
    # https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))
        seen = set()
        for f in folder:
            for i in range(2, len(f)):
                if f[i] == '/' and f[: i] in seen:
                    break
            else:
                seen.add(f)
        return list(seen)

class tester(unittest.TestCase):
    def test_1(self):
        folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        Output= sorted(["/a","/c/d","/c/f"])
        self.assertEqual(Output,sorted(get_sol().removeSubfolders(folder)))
    def test_2(self):
        folder = ["/a","/a/b/c","/a/b/d"]
        Output= ["/a"]
        self.assertEqual(Output,get_sol().removeSubfolders(folder))
    def test_3(self):
        folder = ["/a/b/c","/a/b/ca","/a/b/d"]
        Output= sorted(["/a/b/c","/a/b/ca","/a/b/d"])
        self.assertEqual(Output,sorted(get_sol().removeSubfolders(folder)))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):