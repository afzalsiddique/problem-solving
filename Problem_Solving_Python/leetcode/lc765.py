from collections import Counter;
import unittest; from typing import List;


def get_sol(): return Solution()
# class Solution2:
    # use bfs like leetcode 854

# class Solution3:
#     https://leetcode.com/problems/couples-holding-hands/discuss/1198075/Easy-C%2B%2B-Solution-oror-Full-Documented-Explanation-oror-Very-Easy-Concept


# https://leetcode.com/problems/couples-holding-hands/discuss/336706/The-general-mathematical-idea%3A-permutation-graph-and-graph-decomposition.
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def __repr__(self): return str(self.par)
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
            return self.par[a]
        return a
    def size_of_groups(self):
        for a in range(self.n):
            self.find(a)
        count=Counter(self.par)
        return list(count.values())
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def couple_id(i): return i//2
        uf=UnionFind(len(row)//2)
        i=0
        while i+1<len(row):
            uf.union(couple_id(row[i]),couple_id(row[i+1]))
            i+=2
        ans = uf.size_of_groups()
        no_of_components = len(ans)
        # print(ans)
        return sum(ans) - no_of_components

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minSwapsCouples(row = [0,2,1,3]))
    def test2(self):
        self.assertEqual(0, get_sol().minSwapsCouples(row = [3,2,0,1]))
    def test3(self):
        self.assertEqual(4, get_sol().minSwapsCouples(row = [5,6,4,0,2,1,9,3,8,7,11,10]))
    # def test4(self):
    #     self.assertEqual(1, get_sol().minSwapsCouples(s1 = "ab", s2 = "ba"))
    # def test5(self):
    #     self.assertEqual(1, get_sol().kSimilarity("cba", "abc"))
    # def test6(self):
    #     self.assertEqual(3, get_sol().kSimilarity("bccaba", "abacbc"))
    # def test7(self):
    #     self.assertEqual(3, get_sol().kSimilarity("aabccb", "bbcaca"))