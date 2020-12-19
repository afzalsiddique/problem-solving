from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        for word in strs:
            li.append("".join(sorted(word)))
        di = {}
        for i, word in enumerate(li):
            if word not in di:
                di[word] = [strs[i]]
            else:
                di[word] += [(strs[i])]
        groups = []
        for key in di:
            groups.append(di[key])
        return groups