# import math
#
#
# class Solution:
#     def checkIfPrerequisite(self, n, prerequisites, queries):
#         g = [[math.inf]*n for _ in range(n)]
#         for i in range(n):
#             g[i][i] = 0
#         for i,j in prerequisites:
#             g[i][j] = 1
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     g[i][j] = min(g[i][j], g[i][k]+g[k][j])
#         ans = []
#         for i,j in queries:
#             if g[i][j] != math.inf:
#                 ans.append(True)
#             else:
#                 ans.append(False)
#         return ans

class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        preqs = [set() for _ in range(n)]
        reverse_preqs = [set() for _ in range(n)]
        for preq, course in prerequisites:
            preqs[preq].add(course)
            for p in preqs[course]:
                preqs[preq].add(p)
            for p in reverse_preqs[preq]:
                preqs[p].add(course)
                reverse_preqs[course].add(p)
            reverse_preqs[course].add(preq)
        return [query[1] in preqs[query[0]] for query in queries]