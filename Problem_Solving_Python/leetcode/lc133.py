from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node:Node)->Optional[Node]:
            if not node: return
            if node in clone: return clone[node]
            clone[node]=Node(node.val)
            for neigh in node.neighbors:
                clone[node].neighbors.append(dfs(neigh))
            return clone[node]

        clone:dict[Node,Node]={}
        return dfs(node)
class Solution2:
    # https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
    # recursive dfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(old_node):
            for old_neigh in old_node.neighbors:
                if old_neigh not in clone:
                    new_neigh = Node(old_neigh.val)
                    clone[old_neigh] = new_neigh
                    dfs(old_neigh)
                clone[old_node].neighbors.append(clone[old_neigh])

        if not node:return None
        new_node = Node(node.val)
        clone = {node:new_node}
        dfs(node)
        return new_node

class Solution3:
    # iterative bfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return None
        di = {}
        q = deque([node])
        while q:
            old_node = q.popleft()
            if old_node in di:continue
            di[old_node] = Node(old_node.val)
            for neigh in old_node.neighbors:
                q.append(neigh)

        for old_node in di:
            for neigh in old_node.neighbors:
                di[old_node].neighbors.append(di[neigh])

        return di[node]

def makeGraph(adj:List[List[int]]):
    di={}
    for i,_ in enumerate(adj,1):
        di[i]=Node(i)
    for i,neighs in enumerate(adj,1):
        for neigh in neighs:
            di[i].neighbors.append(di[neigh])
    return di[1]
