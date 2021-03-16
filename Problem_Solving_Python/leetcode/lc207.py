import unittest
from collections import deque
from heapq import *
from typing import List


class Solution:
    # DFS
    # https://www.youtube.com/watch?v=kXy0ABd1vwo
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = ['notvisited' for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visited[i]=='processing':
                return False
            if visited[i]=='visited':
                return True
            visited[i]='processing'
            for v in graph[i]:
                if not dfs(v):
                    return False
            visited[i]='visited'
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    # in degree
    # https://www.youtube.com/watch?v=kXy0ABd1vwo
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for x,y in prerequisites:
            graph[x].append(y)
            indegree[y]+=1

        cnt = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            curr = q.popleft()
            if indegree[curr]==0:
                cnt+=1
            for u in graph[curr]:
                indegree[u]-=1
                if indegree[u]==0:
                    q.append(u)
        if cnt==numCourses:
            return True
        return False
