from collections import deque;
import unittest;


def get_sol(): return Solution()
class Solution:
    # https://miro.medium.com/max/3000/1*MvTnZScOoc6P1ZQR7lzOHg.png
    # https://medium.com/@jolyon129/854-k-similar-strings-7b68772217d0
    def kSimilarity(self, s1: str, s2: str) -> int:
        q=deque()
        n=len(s1)
        s1=list(s1)
        q.append((s1,0))
        res=0
        while q:
            for _ in range(len(q)):
                s1,i=q.popleft()
                j=i
                while i<n and s1[i]==s2[j]:
                    i+=1
                    j+=1
                if i==n: return res
                while i<n:
                    if s1[i]==s2[i]:
                        i+=1
                        continue
                    if s1[i]==s2[j]:
                        tmp=s1[:]
                        tmp[i],tmp[j]=tmp[j],tmp[i]
                        q.append((tmp,j))
                    i+=1
            res+=1


class mytestcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().kSimilarity(s1 = "ab", s2 = "ba"))
    def test2(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abc", s2 = "bca"))
    def test3(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "abac", s2 = "baca"))
    def test4(self):
        self.assertEqual(2, get_sol().kSimilarity(s1 = "aabc", s2 = "abca"))
    def test5(self):
        self.assertEqual(1, get_sol().kSimilarity("cba", "abc"))
    def test6(self):
        self.assertEqual(3, get_sol().kSimilarity("bccaba", "abacbc"))
    def test7(self):
        self.assertEqual(3, get_sol().kSimilarity("aabccb", "bbcaca"))
