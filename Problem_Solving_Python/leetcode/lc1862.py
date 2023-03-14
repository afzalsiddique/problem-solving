import itertools;
import unittest; from typing import List;


def get_sol(): return Solution()
# if num==5:
#   all the numbers in the range [5,10) should contribute 1
#   all the numbers in the range [10,15) should contribute 2
#   all the numbers in the range [15,20) should contribute 3
#  thus the idea of prefix sum comes into picture
class Solution:
    # tle. just add hashmap to avoid tle
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD=10**9+7
        maxx=max(nums)
        freq=[0]*(2*maxx+1)
        for x in nums: freq[x]+=1
        pre=[0]+list(itertools.accumulate(freq))
        res=0
        for num in nums:
            l,r,floorCount=num,2*num-1,1
            while l<=maxx:
                res+=floorCount*(pre[r+1]-pre[l])
                res%=MOD
                l+=num
                r+=num
                floorCount+=1
        return res
class Solution2:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD=10**9+7
        maxx=max(nums)
        freq=[0]*(2*maxx+1)
        for x in nums: freq[x]+=1
        cache={}
        pre=[0]+list(itertools.accumulate(freq))
        res=0
        for num in nums:
            if num in cache:
                res+=cache[num]
                continue
            l,r,floorCount=num,2*num-1,1
            tmp=0
            while l<=maxx:
                tmp+=floorCount*(pre[r+1]-pre[l])
                tmp%=MOD
                l+=num; r+=num;
                floorCount+=1
            cache[num]=tmp
            res+=tmp
            res%=MOD
        return res


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(10,get_sol().sumOfFlooredPairs([5,2,9]))
    def test_2(self):
        self.assertEqual(49,get_sol().sumOfFlooredPairs( [7,7,7,7,7,7,7]))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
