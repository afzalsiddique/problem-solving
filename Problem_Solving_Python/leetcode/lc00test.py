from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1),len(nums2)
        k=min(k,m*n)
        indices = [0]*m
        res = []
        i1=0
        while len(res)<k:
            j1=indices[i1]
            i2=i1+1
            if i2<m:
                j2=indices[i2]
                a = [nums1[i1],nums2[j1]]
                b = [nums1[i2],nums2[j2]]
                if sum(a)<=sum(b):
                    res.append(a)
                    indices[i1]+=1
                    if indices[i1]==n:
                        i1+=1
                else:
                    res.append(b)
                    indices[i2]+=1
            else:
                res.append([nums1[i1],nums2[j1]])
                indices[i1]+=1
        return res


class Correct:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n=len(nums1),len(nums2)
        res=[]
        pq=[]
        for i in range(m):
            a,b=nums1[i],nums2[0]
            heappush(pq,[a+b,a,b,0]) # [sum(key for heap), a,b,idx of nums2]
        while len(res)!=k and pq:
            _,a,b,idx=heappop(pq)
            res.append([a,b])
            idx+=1 # make pair of next number of nums2 and a
            if idx==len(nums2): continue
            new_b=nums2[idx]
            heappush(pq,[a+new_b,a,new_b,idx])
        return res

class Tester(unittest.TestCase):
    def test01(self):
        a,b,k = [-10,-4,0], [3,100], 10
        self.assertEqual(Correct().kSmallestPairs(a,b,k), Solution().kSmallestPairs(a,b,k))
    def test02(self):
        a,b,k = [-10,-4,0,0,6], [3,5,6,7,8,100], 10
        self.assertEqual(Correct().kSmallestPairs(a,b,k), Solution().kSmallestPairs(a,b,k))
    def test03(self):
        a,b,k = [-10,-4,0,0,6], [3,5,6,7,8,100], 10
        self.assertEqual(Correct().kSmallestPairs(a,b,k), Solution().kSmallestPairs(a,b,k))
