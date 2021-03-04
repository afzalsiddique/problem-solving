import unittest
from typing import List


class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0



class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x:(-x.profit, x.deadline))
        s=set()
        ans, cnt = 0, 0
        for job in Jobs:
            profit, deadline = job.profit, job.deadline
            if deadline not in s:
                s.add(deadline)
                ans += profit
                cnt += 1
        return cnt,ans

def create_list_of_jobs(li):
    jobs=[]
    for id, deadline,profit in li:
        jobs.append(Job(deadline, profit))
    return jobs

class MyTestCase(unittest.TestCase):

    def test1(self):
        sol = Solution()
        jobs = create_list_of_jobs([(1,4,20),(2,1,10),(3,1,40),(4,1,30)])
        cnt, prof = sol.JobScheduling(jobs ,4 )
        expected_cnt = 2
        expected_prof = 60
        # self.assertEqual(expected_cnt, cnt)
        self.assertEqual(expected_prof, prof)

    def test_2(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.JobScheduling(0)
        expected = 0
        self.assertEqual(expected, actual)