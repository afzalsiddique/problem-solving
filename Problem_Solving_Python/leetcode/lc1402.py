import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def maxSatisfaction(self, nums:List[int]):
        nums.sort()
        n=len(nums)
        res = 0
        for i,x in enumerate(nums): # cook all the dishes
            res+= x*(i+1)
        running_sum=sum(nums)
        for i in range(n): # start removing from the first dish. Dishes on the left are worse compared to dishes on the right.
            if running_sum<0: # If I do not include the ith item then I can get better res
                res-=running_sum
                running_sum-=nums[i] # subtracting nums[i] means I start from i+1 dish
        return res
class Solution2:
    def maxSatisfaction(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def func(i,mul):
            if i==n: return 0
            res=float('-inf')
            for j in range(i,n):
                option1 = nums[i]*mul + func(i+1,mul+1)
                option2 = func(i+1,mul)
                res=max(res,option1,option2)
            return res

        n=len(nums)
        nums.sort()
        return func(0,1)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(14,get_sol().maxSatisfaction( [-1,-8,0,5,-9]))
    def test2(self):
        self.assertEqual(20,get_sol().maxSatisfaction([4,3,2]))
    def test3(self):
        self.assertEqual(0,get_sol().maxSatisfaction([-1,-4,-5]))
    def test4(self):
        self.assertEqual(35,get_sol().maxSatisfaction([-2,5,-1,0,3,-3]))
    def test5(self):
        self.assertEqual(5640720,get_sol().maxSatisfaction([213,-425,-316,-88,89,-331,191,117,33,442,373,122,209,13,-380,382,-298,436,-255,-108,-45,220,-446,-234,-86,11,223,-232,155,491,267,-13,-438,262,27,184,180,-191,12,-56,334,-4,386,468,281,492,-68,-53,3,258,-421,392,-19,-450,252,-312,-197,-232,-305,397,205,384,-140,-136,444,135,252,333,35,251,189,357,-273,-125,215,411,9,196,-77,73,195,217,104,483,195,92,-128,-454,-42,-155,60,-292,353,441,262,-454,67,-285,271,393,408,128,295,-370,-63,-357,-199,418,482,-240,224,424,-159,-234,377,-162,-22,298,237,198,-105,156,-423,210,427,329,202,-261,-131,-272,92,58,151,-68,-460,-383,99,-362,-397,120,2,-254,384,465,137,-179,-85,309,315,452,470,-346,-189,-263,103,-478,134,258,-469,389,-458,-118,444,-482,59,-78,12,203,262,200,47,-154,246,170,-381,-177,-456,-256,-52,364,-227,-45,280,137,187,203,242,-389,136,-161,-132,420,-31,-138,378,347,31,-419,394,94,441,-3,330,373,93,-424,-336,-320,-117,-171,103,309,-25,-490,-38,356,468,209,306,426,403,-340,-348,-294,-389,488,20,-166,-89,-283,-438,-164,114,495,-357,-61,464,-272]))
    # def test6(self):
    # def test7(self):
    # def test8(self):
