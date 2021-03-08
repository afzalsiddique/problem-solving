# class Solution:
#     def isValid(self, s: str) -> bool:
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        di,q={'(':')','{':'}','[':']'},[]
        for c in s:
            if c in di:
                q.append(c)
            else:
                if not q:return False
                top = q.pop()
                if di[top]==c:continue
                return False
        if not q:
            return True
        return False

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
