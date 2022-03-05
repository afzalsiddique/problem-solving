from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        reverse_g=defaultdict(list)
        incoming={u:0 for u in range(n)}
        for u,v in edges:
            g[u].append(v)
            reverse_g[v].append(u)
            incoming[v]+=1

        q=deque([x for x in incoming if incoming[x]==0])
        res=[set() for _ in range(n)]
        while q:
            node=q.popleft()
            for par in reverse_g[node]:
                res[node]|={par}
                res[node]|=res[par]
            for neigh in g[node]:
                incoming[neigh]-=1
                if incoming[neigh]==0:
                    q.append(neigh)

        return list(map(sorted,res))

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]], get_sol().getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    def test02(self):
        self.assertEqual([[],[0],[0,1],[0,1,2],[0,1,2,3]], get_sol().getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))
    def test03(self):
        self.assertEqual([[],[],[],[],[]], get_sol().getAncestors(5, []))
    def test04(self):
        self.assertEqual([[9],[],[5,7,8],[8],[],[],[1],[8],[],[]], get_sol().getAncestors(10, [[5,2],[8,7],[7,2],[8,3],[1,6],[9,0]]))
