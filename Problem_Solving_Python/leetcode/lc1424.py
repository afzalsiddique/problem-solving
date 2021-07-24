import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # buckets and every bucket is a stack
    # https://leetcode.com/problems/diagonal-traverse-ii/discuss/597741/Clean-Simple-Easiest-Explanation-with-a-picture-and-code-with-comments
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        BIG = 10**5+1
        buckets=[[] for _ in range(BIG)]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                buckets[i+j].append((i,j))
        res=[]
        for k in range(BIG):
            while buckets[k]:
                i,j = buckets[k].pop()
                res.append(nums[i][j])
        return res
class Solution2:
    # bfs
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        m = len(nums)
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            # we only add the number at the bottom if we are at column 0
            if col == 0 and row + 1 < m:
                queue.append((row + 1, col))
            # add the number on the right
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        return ans
class Solution3:
    # sorting
    # time O(nlogn)
    # space O(no of items in the 2d array)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                li.append((i,j))
        li.sort(key=lambda x:(x[0]+x[1],-x[0]))
        res=[]
        for i,j in li:
            res.append(nums[i][j])
        return res
class Solution4:
    # heap
    # time O(nlogn)
    # space O(no of items in the 2d array)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        pq=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                pq.append((i+j,-i,j)) # build heap based on i+j and -i. j is for accessing the item later
        heapify(pq)
        res=[]
        for i in range(len(pq)):
            _,i,j=heappop(pq)
            i*=(-1)
            res.append(nums[i][j])
        return res
class Solution5:
    # tle
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m=len(nums)
        INVALID = 0
        max_col = len(max(nums,key=len)) # https://stackoverflow.com/questions/51453695/in-python-how-to-find-max-length-of-inner-list-in-a-2d-list
        for i in range(m):
            extra=max_col-len(nums[i])
            for _ in range(extra):
                nums[i].append(INVALID)
        # for x in nums: print(x)
        res=[]
        for i in range(m):
            j=0
            while i>=0 and j<max_col:
                if nums[i][j]!=INVALID:
                    res.append(nums[i][j])
                i-=1
                j+=1

        for j in range(1,max_col):
            i=m-1
            while i>=0 and j<max_col:
                if nums[i][j]!=INVALID:
                    res.append(nums[i][j])
                i-=1
                j+=1
        return res


class tester(unittest.TestCase):
    def test_1(self):
        nums = [[1,2,3],[4,5,6],[7,8,9]]
        Output= [1,4,2,7,5,3,8,6,9]
        self.assertEqual(Output, get_sol().findDiagonalOrder(nums))
    def test_2(self):
        nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
        Output= [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        self.assertEqual(Output, get_sol().findDiagonalOrder(nums))
    def test_3(self):
        nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
        Output= [1,4,2,5,3,8,6,9,7,10,11]
        self.assertEqual(Output, get_sol().findDiagonalOrder(nums))
    def test_4(self):
        nums = [[1,2,3,4,5,6]]
        Output= [1,2,3,4,5,6]
        self.assertEqual(Output, get_sol().findDiagonalOrder(nums))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):