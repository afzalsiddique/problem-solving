import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/stone-game-vii/discuss/970268/C%2B%2BPython-O(n-*-n)
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[0] * len(stones) for _ in range(len(stones))]
        pre_sum=list(itertools.accumulate(stones))
        def get_sum(left:int,right:int):
            return pre_sum[right]-pre_sum[left]+stones[left]
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            if dp[i][j] == 0:
                summ = get_sum(i,j)
                other_person_points1 = dfs(i+1,j) # it is a positive number
                other_person_points2 = dfs(i,j-1) # it is a positive number
                my_extra_points1 = summ - stones[i] - other_person_points1
                my_extra_points2 = summ - stones[j] - other_person_points2
                dp[i][j] = max(my_extra_points1,my_extra_points2)
            return dp[i][j]
        res = dfs(0, len(stones) - 1)
        return res

class Solution2:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = {}
        pre_sum=list(itertools.accumulate(stones))
        def get_sum(left:int,right:int):
            return pre_sum[right]-pre_sum[left]+stones[left]
        def dfs(i,j,turn:bool):
            if (i,j,turn) in dp: return dp[i,j,turn]
            if i==j:
                return 0
            summ = get_sum(i,j)
            if turn: # alice's turn
                option1 = summ - stones[i]- dfs(i+1,j,not turn) # treat dfs(...) as a positive number
                option2 = summ - stones[j]- dfs(i,j-1,not turn)
                ans = max(option1,option2)
                dp[i,j,turn] = ans
                return ans
            else: # bob's turn
                option1 = summ - stones[i]- dfs(i+1,j,not turn) # treat dfs(...) as a positive number
                option2 = summ - stones[j]- dfs(i,j-1,not turn)
                ans = max(option1,option2)
                dp[i,j,turn] = ans
                return ans

        return dfs(0,len(stones)-1,True)

class Solution3:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = {}
        pre_sum=list(itertools.accumulate(stones))
        def get_sum(left:int,right:int):
            return pre_sum[right]-pre_sum[left]+stones[left]
        def dfs(i,j,turn:bool):
            if (i,j,turn) in dp: return dp[i,j,turn]
            if i==j:
                return 0
            summ = get_sum(i,j)
            if turn: # alice's turn. maximizer
                option1 = summ - stones[i]+dfs(i+1,j,not turn) # treat dfs(...) as a negative number. because it is coming from minimizer
                option2 = summ - stones[j]+dfs(i,j-1,not turn)
                ans = max(option1,option2)
                dp[i,j,turn] = ans
                return ans
            else: # bob's turn. minimizer
                option1 = summ - stones[i]- dfs(i+1,j,not turn) # treat dfs(...) as a positive number. because it is coming from maximizer
                option2 = summ - stones[j]- dfs(i,j-1,not turn)
                ans = min(-option1,-option2)
                dp[i,j,turn] = ans
                return ans

        return dfs(0,len(stones)-1,True)
class MyTestCase(unittest.TestCase):
    def test_1(self):
        stones = [5,3,1,4,2]
        Output= 6
        self.assertEqual(Output, get_sol().stoneGameVII(stones))
    def test_2(self):
        stones = [7,90,5,1,100,10,10,2]
        Output= 122
        self.assertEqual(Output, get_sol().stoneGameVII(stones))
    def test_3(self):
        stones = [792,195,697,271,743,51,836,322,135,550,399,182,988,25,395,254,480,931,513,772,798,102,110,915,794,330,597,220,789,462]
        Output= 9066
        self.assertEqual(Output, get_sol().stoneGameVII(stones))
    def test_4(self):
        stones = [359,272,421,563,929,261,487,106,398,863,547,691,766,374,117,635,803,487,11,323,931,493,218,831,183,706,968,196,292,332,633,741,515,69,632,949,728,38,613,817,3,706,888,14,667,840,249,365,385,534,31,218,229,680,957,386,598,869,647,496,379,560,706,923,201,895,137,436,683,915,802,751,289,711,216,706,565,404,620,831,639,369,20,760,898,784,375,40,576,123,958,274,488,125,986,855,274,61,582,500,376,54,792,353,110,418,533,661,257,335,869,403,350,499,802,229,21,636,292,326,380,956,629,790,422,354,178,900,414,429,284,242,406,20,474,718,50,768,437,783,803,447,983,854,133,911,647,289,85,833,42,278,698,339,960,801,730,252,802,505,445,375,122,458,42,499,859,453,537,387,641,591,117,799,658,863,79,994,124,296,547,115,148,375,545,31,942,136,393,575,217,984,650,206,782,751,949,428,320,151,232,559,943,19,66,391,207,73,626,708,840,622,410,738,566,387,682,836,231,226,965,172,945,666,658,563,942,975,914,830,597,20,64,552,723,64,354,987,438,972,674,699,498,266,56,215,415,583,924,908,477,405,566,384,934,493,517,295,23,183,51,369,932,145,939,726,83,747,938,777,99,827,754,536,720,819,724,528,211,67,184,572,384,705,648,265,530,939,574,193,423,387,339,17,724,22,857,354,60,53,245,529,124,744,826,833,75,580,799,957,268,177,824,906,986,745,210,638,798,712,102,577,400,697,314,838,61,669,655,859,157,76,4,52,841,58,695,277,86,770,333,777,532,731,819,770,611,435,477,119,563,624,87,173,860,155,421,944,816,635,104,480,262,31,273,893,370,60,525,902,158,14,690,590,14,543,732,400,971,566,202,369,700,706,483,835,200,9,628,752,552,805,887,558,929,116,344,654,658,108,776,718,169,352,689,803,388,508,660,31,857,369,720,569,851,636,952,543,686,607,73,484,747,482,822,182,385,631,236,625,981,584,844,378,441,840,405,417,612,321,275,189,211,10,123,681,300,845,412,529,278,670,346,212,696,96,296,326,958,45,88,833,301,905,693,838,697,758,479,221,463,254,978,866,207,772,496,991,44,587,212,225,5,873,672,199,582,816,924,713,517,208,135,292,779,547,606,158,269,953,260,254,608,681,117,429,23,618,530,185,630,238,660,166,189,594,545,763,744,637,41,671,742,560,570,806,392,669,935,284,522,576,885,636,934,706,478,592,519,83,367,933,424,495,451,222,324,6,813,119,418,825,397,232,322,650,860,413,536,893,396,742,210,471,518,124,987,699,544,494,255,793,428,905,531,342,663,762,579,239,214,290,1000,21,359,855,559,70,703,954,101,542,838,256,752,583,686,165,467,729,391,568,575,920,202,407,341,136,104,45,175,597,875,579,731,384,335,748,325,798,363,626,153,434,155,438,107,244,723,614,207,768,191,875,885,835,599,373,573,575,403,477,508,105,915,299,207,355,452,40,965,543,874,177,758,825,295,961,399,335,775,735,388,689,8,592,197,455,80,668,205,533,234,56,688,637,433,935,479,568,377,495,415,250,820,641,717,156,430,723,914,816,611,823,503,98,218,679,355,865,199,658,766,428,312,896,247,206,544,648,854,835,849,409,223,764,720,528,354,570,182,944,569,950,93,515,206,174,974,643,274,330,39,549,16,879,865,494,798,494,801,220,402,515,773,487,512,929,346,165,935,545,150,424,659,533,480,265,78,935,586,794,944,580,999,509,505,625,348,381,302,428,468,935,456,746,223,39,566,243,342,458,24,374,569,108,286,83,963,846,824,110,179,788,569,532,214,442,535,906,266,913,806,11,421,241,306,781,823,748,992,200,338,787,597,439,230,114,808,980,398,255,75,437,17,659,435,837,81,427,546,3,421,649,578,842,637,181,943,269,503,782,776,389,931,777,157,468,392,487,1,917,590,60,692,108,402,31,279,547,723,141,894,458,298,416,318,596,770,583,720,272,660,304,940,170,743,658,848,603,335,323,559,72,980,91,782,958,981,15,46,955,856,796,719,919,88,213,268,595,245,393,417,324,737,22,994,209,343,596,275,666,932,398,960]
        Output= 227354
        self.assertEqual(Output, get_sol().stoneGameVII(stones))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
