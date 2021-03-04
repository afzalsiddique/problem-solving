# same as n meetings in one room
import unittest


def maximumActivities(n,start,end):
    activities = sorted(zip(start,end), key = lambda x:x[1]) # sort by finish time
    last, cnt = 0,0
    for s,e in activities:
        if last<=s:
            cnt+=1
            last = e
    return cnt



class MyTestCase(unittest.TestCase):

    def test_1(self):
        start = [10,12,20]
        end = [20,25,30]
        actual = maximumActivities(len(start),start, end)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        start = [1,3,0,5,8,5]
        end = [2,4,6,7,9,9]
        actual = maximumActivities(len(start),start, end)
        expected = 4
        self.assertEqual(expected, actual)