import unittest
from leetcode.leetcode395 import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'ababb'
        k = 2
        actual = solution.isValid(s, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = 'ababbc'
        k = 2
        actual = solution.isValid(s, k)
        expected = False
        self.assertEqual(expected, actual)

    # def test_7(self):
    #     solution = Solution()
    #     s = ''
    #     k = 2
    #     actual = solution.isValid(s, k)
    #     expected = False
    #     self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = 'ababbc'
        k = 2
        actual = solution.tell_me_where_to_divide(s, k)
        expected = [5]
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = 'abacabbc'
        k = 3
        actual = solution.tell_me_where_to_divide(s, k)
        expected = [3,7]
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        s = 'ababababbabcabababbacbabaaab'
        indices = [11,20]
        actual = solution.divide_and_return(s, indices)
        actual = sorted(actual)
        expected = sorted(['ababababbab','abababba', 'babaaab'])
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        s = 'ababaaabcc'
        indices = [8,9]
        actual = solution.divide_and_return(s, indices)
        actual = sorted(actual)
        expected = sorted(['ababaaab','', ''])
        self.assertEqual(expected, actual)

    def test_8(self):
        solution = Solution()
        s = 'aaabb'
        k = 3
        actual = solution.longestSubstring(s, k)
        expected = 3
        self.assertEqual(expected, actual)

    def test_9(self):
        solution = Solution()
        s = 'ababbc'
        k = 2
        actual = solution.longestSubstring(s, k)
        expected = 5
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
