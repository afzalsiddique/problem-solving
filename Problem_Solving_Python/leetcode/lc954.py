import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n=len(arr)
        arr.sort() # why do need to sort?
        # for example [4,2,16,8]
        # 2 it's the smallest and we know there is no x//2 left.
        # So we know we need to find 2x
        # and we will not do this -> [4,8,...]
        count=Counter(arr)

        res=[] # could by replaced by a variable
        for x in arr:
            if count[x]:
                count[x]-=1
                if count[2*x]:
                    count[2*x]-=1
                    res.append(x)
                    res.append(2*x)
                else:
                    count[x]+=1
        # print(res)
        # print(n,len(res))
        # print(count)
        if len(res)==n: return True
        return False
class Solution3:
    # wrong
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n=len(arr)
        arr.sort()
        count=Counter(arr)

        res=[]
        for x in arr:
            if count[x] and count[2*x]:
                count[x]-=1
                count[2*x]-=1
                res.append(x)
                res.append(2*x)
        # print(res)
        # print(n,len(res))
        # print(count)
        if len(res)==n: return True
        return False
class Solution2:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n=len(arr)
        arr.sort()
        count1=Counter(arr) # count1 and res1 is enough
        count2=Counter(arr)

        res1=[] # could be replaced by two variables
        res2=[]
        for x in arr:
            if count1[x]:
                count1[x]-=1
                if count1[2*x]:
                    count1[2*x]-=1
                    res1.append(x)
                    res1.append(2*x)
                else:
                    count1[x]+=1
            if x%2==0 and count2[x]:
                count2[x]-=1
                if count2[x//2]:
                    count2[x//2]-=1
                    res2.append(x//2)
                    res2.append(x)
                else:
                    count2[x]+=1
        # print(res1)
        # print(res2)
        # print(n,len(res1),len(res2))
        # print(count1)
        # print(count2)
        if len(res1)==n or len(res2)==n: return True
        return False

class tester(unittest.TestCase):
    def test_1(self):
        arr = [3,1,3,6]
        Output= False
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_2(self):
        arr = [2,1,2,6]
        Output= False
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_3(self):
        arr = [4,-2,2,-4]
        Output= True
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_4(self):
        arr = [1,2,4,16,8,4]
        Output= False
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_5(self):
        arr = [-33,0]
        Output= False
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_6(self):
        arr = [0,0]
        Output= True
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_7(self):
        arr = [-62,86,96,-18,43,-24,-76,13,-31,-26,-88,-13,96,-44,9,-20,-42,100,-44,-24,-36,28,-32,58,-72,20,48,-36,-45,14,24,-64,-90,-44,-16,86,-33,48,26,29,-84,10,46,50,-66,-8,-38,92,-19,43,48,-38,-22,18,-32,-48,-64,-10,-22,-48]
        Output= True
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_8(self):
        arr = [8,2,16,4]
        Output= True
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))
    def test_9(self):
        arr = [8,4,4,2]
        Output= True
        self.assertEqual(Output, get_sol().canReorderDoubled(arr))

