# class Solution:
#     def isValid(self, s: str) -> bool:
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        di = {'{':'}','[':']','(':')'}
        for c in s:
            if c not in di: # if closing
                if not st:return False # closing coming before opening
                if di[st[-1]] != c:return False # closing coming with corresponding opening
                st.pop()
            else: # if opening
                st.append(c)
        if st:
            return False
        return True

class MyTestClass(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        actual = solution.isValid("()")
        expected = True
        self.assertEqual(expected, actual)
    def test_2(self):
        solution = Solution()
        actual = solution.isValid("()[]{}")
        expected = True
        self.assertEqual(expected, actual)
    def test_3(self):
        solution = Solution()
        actual = solution.isValid("(]")
        expected = False
        self.assertEqual(expected, actual)
    def test_4(self):
        solution = Solution()
        actual = solution.isValid("([)]")
        expected = False
        self.assertEqual(expected, actual)
    def test_5(self):
        solution = Solution()
        actual = solution.isValid("]")
        expected = False
        self.assertEqual(expected, actual)
