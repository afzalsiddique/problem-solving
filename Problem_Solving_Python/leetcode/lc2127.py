from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
    def maximumInvitations(self, A: List[int]) -> int:
        # First, we find the largest circle.
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):

            # If a people hasn't been visited:
            if seen[idx] == 0:

                # start is for locating the first visited people, cur_people stands
                #for the current people we are visiting, we use curset to store all
                # the visited people in this iteration.
                start = idx
            cur_people = idx
            curset = set()

            # As long as we are visiting new people, we keep finding his/her favorite.
            while seen[cur_people] == 0:
                seen[cur_people] = 1
                curset.add(cur_people)
                cur_people = A[cur_people]

                # Until we find the first visited people. Depends on if this
                # visited people has been visited in eariler iteration or just this iteration.
                if cur_people in curset:       # if current people is in current set, meaning we have found a new circle
                    cursum = len(curset)

            # use 'start' to find the distance from the first visited people in this iteration
            # to this current people.
            while start != cur_people:
                cursum -= 1
                start = A[start]
            maxc = max(maxc, cursum)

        # Then we try to find the sum of largest arms. Firstly, find all mutual-favorite peoples.
        pair = []
        visited = [0] * n
        for i in range(n):

            # If a is b's favorite and vise versa, we put them in 'pair'.
            if A[A[i]] == i and visited[i] == 0:
            # alternative
            # if A[A[i]] == i and (i,A[i]) not in pair and (A[i],i) not in pair: # use pair as set
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1

        # for every people I, find out all the people whos favorite is I.
        res = 0
        child = defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)

        for a, b in pair:
            # max arm length start from first people a
            maxa = 0
            dq = deque()
            for node in child[a]:
                if node != b:
                    dq.append([node, 1]) # (node,depth)
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n) # take the max depth
                for neigh in child[cur]:
                    dq.append([neigh, n + 1]) # (node,depth+1)

            # max arm length start from first people b
            maxb = 0
            dq = deque()
            for node in child[b]:
                if node != a:
                    dq.append([node, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for neigh in child[cur]:
                    dq.append([neigh, n + 1])

                # Thus the total length is the two longest arm plus 2 (a and b themselves)
            res += 2 + maxa + maxb

        # select the larger one as the answer.
        return max(maxc, res)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().maximumInvitations([2,2,1,2]))
    def test2(self):
        self.assertEqual(3, get_sol().maximumInvitations([1,2,0]))
    def test3(self):
        self.assertEqual(4, get_sol().maximumInvitations([3,0,1,4,1]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
