# https://www.youtube.com/watch?v=dxVcMDI7vyI&t=333s
import unittest


class Solution:
    def solve(self, A):
        cnt,maxx=0,float('-inf')
        start = [(A[i][0],True) for i in range(len(A))]
        end = [(A[i][1],False) for i in range(len(A))]
        al = start+end
        al.sort()
        for time,arrival in al:
            if arrival:
                cnt+=1
                maxx=max(maxx,cnt)
            else:
                cnt-=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        A = [[0, 30], [5, 10], [15, 20] ]
        actual = Solution().solve(A)
        expected = 2
        self.assertEqual(expected,actual)
    def test_2(self):
        A =  [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13] ]
        actual = Solution().solve(A)
        expected = 4
        self.assertEqual(expected,actual)


def findPlatform(n, arr, dep):
    # I could be in the stations watching over all the platforms.
    # I only need to consider when highest no of trains are sitting in the platforms.
    # that's why arrivals and departures could be sorted individually
    arr.sort()
    dep.sort()
    cnt,maxx=0,0
    i,j=0,0
    while i!=n:
        if arr[i]<=dep[j]:
            cnt+=1
            i+=1
        else:
            cnt-=1
            j+=1
        maxx=max(maxx,cnt)
    return maxx

arrivals= [900, 940, 950, 1100, 1500, 1800]
departures=[ 910, 1200, 1120, 1130, 1900, 2000 ]
print(findPlatform(len(arrivals),arrivals,departures))


arrivals= [900, 940]
departures=[ 910, 1200]
print(findPlatform(len(arrivals), arrivals,departures))

arrivals= [1100, 1500, 1800]
departures=[1130, 1900, 2000]
print(findPlatform(len(arrivals), arrivals,departures))