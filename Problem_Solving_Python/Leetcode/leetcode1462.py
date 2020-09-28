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