import unittest


def maxLen(n, arr):
    di = {}
    curr_sum,maxx= 0,0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum==0: # [0,0,0,0], [-1,1,-1,1]
            maxx = i+1
        if curr_sum in di:
            maxx = max(maxx, i-di[curr_sum])
        else:
            di[curr_sum] = i
    return maxx
    # another version. dictionary initialized
    di = {0:-1}
    curr_sum,maxx= 0,0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum in di:
            maxx = max(maxx, i-di[curr_sum])
        else:
            di[curr_sum] = i
    return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums=[15,-2,2,-8,1,7,10,23]
        actual = maxLen(len(nums),nums)
        expectd = 5
        self.assertEqual(expectd, actual)
    def test_2(self):
        nums=[0,0,0,0]
        actual = maxLen(len(nums),nums)
        expectd = 4
        self.assertEqual(expectd, actual)
    def test_3(self):
        nums=[-1,1,-1,1]
        actual = maxLen(len(nums),nums)
        expectd = 4
        self.assertEqual(expectd, actual)
    def test_4(self):
        nums=[1,2,34,5,6,5,3]
        actual = maxLen(len(nums),nums)
        expectd = 0
        self.assertEqual(expectd, actual)
