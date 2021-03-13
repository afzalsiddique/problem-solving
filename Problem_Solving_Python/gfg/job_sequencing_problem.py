import unittest
from typing import List


class Job:
    def __init__(self, deadline, profit, id):
        self.profit = profit
        self.deadline = deadline
        self.id = id

    def __repr__(self):
        return str(self.profit)+" "+str(self.deadline)


class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x:-x.profit)
        highest=0 # maximum deadline
        for job in Jobs:
            if job.deadline>highest:
                highest=job.deadline
        cnt,ans = 0,0
        seq=[-1]*highest # this array holds the sequence of job ids in the order they should be scheduled
        for job in Jobs:
            tmp=job.deadline-1 # '-1' deadline is 1-indexed. You can't do any job at 0-th day
            while True:
                if seq[tmp]==-1: # found space
                    break
                if tmp==0: # reached very beginning
                    break
                tmp-=1
            if seq[tmp]==-1: # found space
                seq[tmp]=job.id
                ans+=job.profit
                cnt+=1
        return cnt,ans

    def create_list_of_jobs(self,li):
        jobs=[]
        for id, deadline,profit in li:
            jobs.append(Job(deadline, profit, id))
        return jobs

class MyTestCase(unittest.TestCase):

    def test1(self):
        sol = Solution()
        jobs = sol.create_list_of_jobs([(1,4,20),(2,1,10),(3,1,40),(4,1,30)])
        cnt, prof = sol.JobScheduling(jobs,len(jobs))
        expected_cnt = 2
        expected_prof = 60
        self.assertEqual(expected_cnt, cnt)
        self.assertEqual(expected_prof, prof)

    def test2(self):
        sol = Solution()
        jobs = sol.create_list_of_jobs([(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)])
        cnt, prof = sol.JobScheduling(jobs,len(jobs))
        expected_cnt = 2
        expected_prof = 127
        self.assertEqual(expected_cnt, cnt)
        self.assertEqual(expected_prof, prof)

    def test3(self):
        sol = Solution()
        jobs = sol.create_list_of_jobs([(1, 2, 100), (2, 1, 19), (3, 2, 25), (4, 1, 27), (5, 1, 15)])
        cnt, prof = sol.JobScheduling(jobs,len(jobs))
        expected_cnt = 2
        expected_prof = 127
        self.assertEqual(expected_cnt, cnt)
        self.assertEqual(expected_prof, prof)

