# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    # recursive dfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return None
        new_node = Node(node.val)
        di = {node:new_node}

        def dfs(old_node):
            for old_neigh in old_node.neighbors:
                if old_neigh not in di:
                    new_neigh = Node(old_neigh.data)
                    di[old_neigh] = new_neigh
                    dfs(old_neigh)
                di[old_node].neighbors.append(di[old_neigh])

        dfs(node)
        return new_node

    # iterative bfs
    def cloneGraph2(self, node: 'Node') -> 'Node':
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
