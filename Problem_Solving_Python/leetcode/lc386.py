import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n)
    # space complexity is probably O(no of digits in n) = O(1) -> run space complexity checker
    # The idea is pretty simple. If we look at the order we can find out we just keep adding digit from 0 to 9 to every digit and make it a tree.
    # Then we visit every node in pre-order.
    #     1        2        3    ...         9        range -> (1...9)
    #    /\        /\       /\             /  \
    # 10 ...19  20...29  30...39   ....   90...99     range -> (0...9)
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        def dfs(cur):
            if cur>n: return
            res.append(cur)
            for i in range(9+1): # including 9
                dfs(cur*10+i)

        for i in range(1,9+1): # including 9
            dfs(i)
        return res
class Solution2:
    # time O(nlogn) space O(n)
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1,n+1)]
        nums.sort()
        return list(map(int,nums))


class tester(unittest.TestCase):
    def test01(self):
        n = 13
        Output= [1,10,11,12,13,2,3,4,5,6,7,8,9]
        self.assertEqual(Output, get_sol().lexicalOrder(n))
    def test02(self):
        n = 2
        Output= [1,2]
        self.assertEqual(Output, get_sol().lexicalOrder(n))


class SpaceComplexity:
    max_depth = 0
    def space_complexity_checker(self, n: int):
        res=[]
        def dfs(cur,depth):
            if depth>self.max_depth: self.max_depth=depth
            if cur>n: return
            res.append(cur)
            for i in range(9+1): # including 9
                dfs(cur*10+i,depth+1)

        for i in range(1,9+1): # including 9
            dfs(i,1)
        print("n: {:<6} depth: {:<6}".format(n,self.max_depth))
        return self.max_depth

class space_complexity_tester(unittest.TestCase):
    def test01(self):
        maxx=float('-inf')
        no_of_test=10
        for _ in range(no_of_test):
            n=random.randint(100,5*10000)
            maxx=max(maxx,SpaceComplexity().space_complexity_checker(n))
        print("maximum depth: {}".format(maxx))
