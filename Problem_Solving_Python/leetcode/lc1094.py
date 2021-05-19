import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # Process all trips, adding passenger count to the start location, and removing it from the end location. After
    # processing all trips, a positive value for the specific location tells that we are getting more passengers;
    # negative - more empty seats. Finally, scan all stops and check if we ever exceed our vehicle capacity.

    # In Java, this could be done using TreeMap
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = defaultdict(int)
        for trip in trips:
            stops[trip[1]] += trip[0]
            stops[trip[2]] -= trip[0]
        cur = 0
        for s in sorted(stops.keys()):
            cur += stops[s]
            if cur > capacity:
                return False
        return True
class Solution2:
    # https://leetcode.com/problems/car-pooling/discuss/857489/Python-linear-solution-using-cumulative-sums-explained
    # cumulative sum
    def carPooling(self, trips, capacity):
        m = max(i for _,_,i in trips)
        times = [0]*(m+1)
        for i,j,k in trips:
            times[j] += i
            times[k] -= i
        return max(itertools.accumulate(times)) <= capacity

# class Solution3:
    # heap

class Solution4:
    # wrong
    # similar approach to minimum platforms does not work
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n=len(trips)
        trips.sort(key=lambda x:x[2])
        print(trips)
        i=0 # for pickup
        j=0 # for dropoff
        current_capacity=0
        while i<n:
            pickup_time=trips[i][1]
            dropoff_time = trips[j][2]
            passenger_pickup=trips[i][0]
            passenger_dropoff=trips[j][0]
            if pickup_time<dropoff_time:
                current_capacity+=passenger_pickup
                i+=1
                if current_capacity>capacity: return False
            else:
                current_capacity-=passenger_dropoff
                j+=1
        return True

class tester(unittest.TestCase):
    def test1(self):
        trips = [[2,1,5],[3,3,7]]
        capacity = 4
        Output= False
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test2(self):
        trips = [[2,1,5],[3,3,7]]
        capacity = 5
        Output= True
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test3(self):
        trips = [[2,1,5],[3,5,7]]
        capacity = 4
        Output= True
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test4(self):
        trips = [[2,1,5],[3,5,7]]
        capacity = 3
        Output= True
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test5(self):
        trips = [[3,2,7],[3,7,9],[8,3,9]]
        capacity = 11
        Output= True
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test6(self):
        trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
        capacity = 23
        Output= True
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
    def test7(self):
        trips = [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]]
        capacity = 28
        Output= False
        self.assertEqual(Output,Solution().carPooling(trips, capacity))
