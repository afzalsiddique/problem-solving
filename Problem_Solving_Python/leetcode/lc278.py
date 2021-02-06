import unittest


class Solution:
    def firstBadVersion(self, n, first_bad):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(n):
            if n>=first_bad:
                return True
            return False

        lo = 1
        hi = n+1
        while lo<hi:
            mid = (lo+hi)//2
            if isBadVersion(mid)==False:
                lo = mid+1
            else:
                hi = mid
        return lo

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 1
        actual = sol.firstBadVersion(1,1)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 4
        actual = sol.firstBadVersion(5,4)
        self.assertEqual(expected, actual)