# https://www.geeksforgeeks.org/floor-value-kth-root-of-a-number-using-recursive-binary-search/
import unittest


class Solution:
    def power(self, x, n):

        if (n == 0):
            return 1
        temp = self.power(x, n // 2)
        if (n % 2 == 0):
            return temp * temp
        else:
            return x * temp * temp
    def NthRoot(self, n, x):


        def nthRootSearch(low, high, x, n):
            if low > high: return -1
            if (low <= high):
                mid = (low + high) // 2
                # Base Case
                if self.power(mid, n) == x:
                    return mid

                temp = self.power(mid, n)
                if temp < x:
                    return nthRootSearch(mid + 1, high, x, n)
                else:
                    return nthRootSearch(low, mid - 1, x, n)

            return low



        return nthRootSearch(0,x,x,n)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.NthRoot(2,64)
        expected = 8
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.NthRoot(2, 63)
        expected = -1
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = solution.NthRoot(6,64)
        expected = 2
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = solution.NthRoot(2,9)
        expected = 3
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = solution.NthRoot(3,9)
        expected = -1
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        actual = solution.power(4,2)
        expected = 16
        self.assertEqual(expected, actual)

    def test_7(self):
        solution = Solution()
        actual = solution.power(3,3)
        expected = 27
        self.assertEqual(expected, actual)