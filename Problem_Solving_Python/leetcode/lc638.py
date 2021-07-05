import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/shopping-offers/discuss/105204/Python-dfs-with-memorization.
    # dfs + dp
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp={}
        def helper(needs):
            if needs in dp: return dp[needs]
            if min(needs)<0: return float('inf') # bought more than required
            minn = sum(price[i]*needs[i] for i in range(len(price))) # calculate price without any offers
            for offer in special:
                new_need = tuple([i-j for i,j in zip(needs,offer)])
                offer_price= offer[-1]
                minn=min(minn,offer_price+helper(new_need))
            dp[needs]=minn
            return minn

        return helper(tuple(needs))
class Solution2:
    # backtracking
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        res=[]
        def helper(start,need:List[int],total):
            for x in need:
                if x<0: return
            if sum(need)==0:
                res.append(total)
                return
            for i in range(start,len(special)):
                for j in range(len(need)):
                    need[j]-=special[i][j]
                helper(i,need,total+special[i][-1])
                for j in range(len(need)):
                    need[j]+=special[i][j]

        for i in range(len(price)): # adding regular prices as special offers
            tmp=[0]*len(special[i])
            tmp[i]=1
            tmp[-1]=price[i]
            special.append(tmp)

        # print(special)
        helper(0,needs,0)
        return min(res)


class MyTestCase(unittest.TestCase):
    def test_01(self):
        price = [2,5]
        special = [[3,0,5],[1,2,10]]
        needs = [3,2]
        Output= 14
        self.assertEqual(Output,get_sol().shoppingOffers(price,special,needs))
    def test_02(self):
        price = [2,3,4]
        special = [[1,1,0,4],[2,2,1,9]]
        needs = [1,2,1]
        Output= 11
        self.assertEqual(Output,get_sol().shoppingOffers(price,special,needs))
    # def test_03(self):
    # def test_04(self):
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):

