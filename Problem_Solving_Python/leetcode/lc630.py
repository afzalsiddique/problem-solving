from heapq import *; import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=ey8FxYsFAMU
    # For any iteration check if taking the course, total_time will exceed the deadline
    # 1. If no, then just add the course time to the total time
    # 2. If yes, then swap with the course which has the longest duration.
    #    Swapping with longer duration course will reduce total_time.
    #    To get the longest duration we need to have a max_heap.
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        pq=[]
        total_time=0
        for time,deadline in courses:
            total_time+=time
            heappush(pq,-time)
            if total_time>deadline:
                tmp=heappop(pq)*(-1)
                total_time-=tmp
        return len(pq)
class Solution2:
    # dp. tle
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def func(i,cur_time):
            if i==n: return 0
            this_time,deadline=courses[i]
            maxx=float('-inf')
            if cur_time+this_time<=deadline: # take this course
                maxx=max(maxx,func(i+1,cur_time+this_time)+1)
            maxx=max(maxx,func(i+1,cur_time)) # do not take this course
            return maxx

        n=len(courses)
        courses.sort(key=lambda x:x[1])
        return func(0,0)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().scheduleCourse(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]))
    def test2(self):
        self.assertEqual(1, get_sol().scheduleCourse(courses = [[1,2]]))
    def test3(self):
        self.assertEqual(0, get_sol().scheduleCourse(courses = [[3,2],[4,3]]))
    def test4(self):
        self.assertEqual(4, get_sol().scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
