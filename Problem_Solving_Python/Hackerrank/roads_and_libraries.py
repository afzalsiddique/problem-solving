import collections


class Solution:
    def roadsAndLibraries(self, n, c_lib, c_road, cities):
        def dfs(i):
            visited.add(i)
            if i not in d:  # if i itself is a component
                return 1    #if i doesn't have any neighbor
            no_of_items_in_a_component = 1
            for neighbor in d[i]:
                if neighbor not in visited:
                    no_of_items_in_a_component += dfs(neighbor)
            return no_of_items_in_a_component

        if c_road > c_lib:
            return n * c_lib
        visited = set()
        d = collections.defaultdict(list)
        for c1, c2 in cities:
            d[c1].append(c2)
            d[c2].append(c1)
        group = []
        for i in range(1, n + 1):
            if i not in visited:
                group.append(dfs(i))
        return n * c_road + (c_lib - c_road) * len(group)
