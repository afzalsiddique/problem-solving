from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        pq=[]
        maxx=float('-inf')
        minn=float('inf')
        for i in range(n):
            val=nums[i][0]
            maxx=max(maxx,val)
            minn=min(minn,val)
            heappush(pq,[val,i,0])

        resVal=maxx-minn
        res=[minn,maxx]
        while len(pq)==len(nums):
            tmpMin,i,j=heappop(pq)
            if maxx-tmpMin<resVal:
                resVal=maxx-tmpMin
                res=[tmpMin,maxx]

            if j+1<len(nums[i]):
                newVal=nums[i][j+1]
                maxx=max(maxx,newVal)
                heappush(pq,[newVal,i,j+1])
            else:
                break
        return res



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([20,24], get_sol().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
    def test02(self):
        self.assertEqual([1,1], get_sol().smallestRange([[1,2,3],[1,2,3],[1,2,3]]))
    def test03(self):
        self.assertEqual([10,11], get_sol().smallestRange([[10,10],[11,11]]))
    def test04(self):
        self.assertEqual([10,11], get_sol().smallestRange([[10],[11]]))
    def test05(self):
        self.assertEqual([1,7], get_sol().smallestRange([[1],[2],[3],[4],[5],[6],[7]]))
    def test06(self):
        self.assertEqual([5819, 55460], get_sol().smallestRange([[24992,50748,95744,95883,96215,96220,96228,96261,96262,96282,96283,96298,96300,96301,96302],[-49982,-30856,-18263,7707,14170,14403,16538,16590,16609,16624,16633],[-2278,3082,4526,4584,5656,5774,5789,5818,5819],[3350,52729,52767,52894,53034,53037,53062,53069,53069,53073],[-37125,5045,6966,13789,16629,19193,20841,32593,33460,33561,33583,33750,33770,33774,33775,33776,33777,33782],[2695,13193,22821,33445,34016,35303,35634,35975,35994,36193,36244,36268,36272],[22400,23016,27567,49766,51312,53582,53832,53852,53866,53867,53871,53871,53871,53871,53873],[40102,58020,86502,88062,88626,88645,88645,88650,88650,88651],[8493,57620,58817,60167,60204,60531,60742,60751,60846,60873,60880,60889,60890,60892,60892,60893],[-18345,12083,12184,15480,15503,15527,15537,15542],[-55646,26553,27767,30264,33045,35099,37668,37736,37814,37918,37923,37929,37931,37932],[55460,85320,87101,87138,87290,87402,87432,87467,87485,87504,87504,87504,87505],[47076,47436,47738,63970,70611,78538,79347,79376,79455,79463,79493,79497,79497,79498,79502]]))
    # def test07(self):
    # def test08(self):
