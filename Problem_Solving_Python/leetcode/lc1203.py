from collections import defaultdict;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=I4Vwkq7e2xE&t=480s
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: List[List[int]]) -> List[int]:
        def getEntry(i:int):
            groupNo=group[i]
            if groupNo==-1:
                return i
            return n+2*groupNo
        def getExit(i:int):
            groupNo=group[i]
            if groupNo==-1:
                return i
            return n+2*groupNo+1
        g={i:[] for i in range(n+2*m)}
        for i in range(n):
            if group[i]!=-1:
                # every group has an entry and exit point
                g[getEntry(i)].append(i) # connect every node in a group to the entry point of the group
                g[i].append(getExit(i)) # connect every node in a group to the exit point of the group

            for j in beforeItems[i]:
                a,b=i,j
                if group[i]!=group[j]: # inter group connection
                    a=getEntry(i)
                    b=getExit(j)
                g[b].append(a) # inter group + intra group

        res=self.topological_sort_dfs_stack_visited(g)
        return list(filter(lambda x:0<=x<n, res))
    def topological_sort_dfs_stack_visited(self, graph): # leetcode 210
        def dfs(u):
            if visited[u]==PROCESSING: # loop found
                return False
            if visited[u]==VISITED: return True
            visited[u]=PROCESSING
            for v in graph[u]:
                if not dfs(v): return False
            visited[u]=VISITED
            res.append(u)
            return True

        NOT_VISITED=0; VISITED=1; PROCESSING=-1
        visited = [NOT_VISITED]*len(graph)
        res = []
        for i in range(len(graph)-1,-1,-1):
            if not dfs(i): return []
        return res[::-1]
class Solution2:
    # wrong
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        PROCESSING,VISITED,NOT_VISITED=-1,1,0
        def dfs(u):
            if state[u]==PROCESSING:
                return False
            if state[u]==VISITED:
                return True
            state[u]=PROCESSING
            for v in g[u]:
                if not dfs(v):
                    return False
            state[u]=VISITED
            res.append(u)
            return True

        beforeItems=[set(beforeItems[i]) for i in range(len(beforeItems))]

        di=defaultdict(set)
        par={}
        for node, groupNo in enumerate(group):
            if groupNo!=-1:
                di[groupNo].add(node)
            par[node]=groupNo

        state=[NOT_VISITED]*n
        g=defaultdict(set)
        for x in range(len(beforeItems)):
            for y in beforeItems[x]:
                g[y].add(x)
                for z in range(n):
                    if y!=z and z!=x and par[y]!=-1 and par[y]==par[z] and y not in beforeItems[x]:
                        g[z].add(x)

        # print(g)
        res=[]
        for u in range(n):
            if not dfs(u):
                return []
        return res[::-1]


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertIn(get_sol().sortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]),[[6,3,4,1,5,2,0,7],[0,7,6,3,4,1,5,2]])
    def test_2(self):
        self.assertEqual([],get_sol().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))
    def test_3(self):
        self.assertIn(get_sol().sortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]),[[3,2,4,1,0],[2,4,1,3,0]])
    # def test_4(self):
