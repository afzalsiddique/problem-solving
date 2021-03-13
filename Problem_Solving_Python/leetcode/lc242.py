from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        if m!=n:return False
        di = defaultdict(int)
        for i in range(m):
            di[s[i]]+=1
            di[t[i]]-=1
        for c in di:
            if di[c]!=0:
                return False
        return True
    def isAnagram_(self, s: str, t: str) -> bool:
        di1 = defaultdict(int)
        di2 = defaultdict(int)
        for c in s:
            di1[c] += 1
        for c in t:
            di2[c] += 1
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if di1[c] != di2[c]:
                return False
        return True
