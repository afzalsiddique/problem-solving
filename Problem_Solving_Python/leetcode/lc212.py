from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

# Trie class same as leetcode 208
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isWord = True

class Solution:
    def findWords(self, board, words):
        res = []
        def dfs(node, i, j, path):
            if node.isWord:
                res.append(path)
                node.isWord = False
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = "#"
            dfs(node, i+1, j, path+tmp)
            dfs(node, i-1, j, path+tmp)
            dfs(node, i, j-1, path+tmp)
            dfs(node, i, j+1, path+tmp)
            board[i][j] = tmp

        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(node, i, j, "")
        return res

# dfs+backtrack. TLE. time: O(n*m  *  n*m  * no_of_words)
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n=len(board),len(board[0])
        sett = set()
        def dfs(x,y,word,path):
            if len(word)==0:
                sett.add(''.join(path))
                return
            if x>=m or y>=n or x<0 or y<0:
                return
            if board[x][y]=='#':return
            first_letter = word[0]
            if board[x][y]==first_letter:
                prev_letter = board[x][y]
                board[x][y]='#'
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    row,col = x+dx, y+dy
                    dfs(row,col, word[1:], path+[first_letter])
                board[x][y]=prev_letter

        for i in range(m):
            for j in range(n):
                for word in words:
                    dfs(i,j,word, [])
        return list(sett)

class mycase(unittest.TestCase):
    def test1(self):
        expected = sorted(["eat","oath"])
        actual = sorted(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
        self.assertEqual(expected,actual )
    def test2(self):
        expected = sorted(Solution().findWords([["a","b"],["c","d"]], ["abcb"]))
        actual = sorted([])
        self.assertEqual(expected,actual )
    def test3(self):
        expected = sorted(Solution().findWords([['a']], ['a']))
        actual = sorted(['a'])
        self.assertEqual(expected, actual)
    def test4(self):
        expected = sorted(["abcdefg","befa","eaabcdgfa","gfedcbaaa"])
        actual = sorted(Solution().findWords([["a","b","c"],["a","e","d"],["a","f","g"]],["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]))
        self.assertEqual(expected, actual)
