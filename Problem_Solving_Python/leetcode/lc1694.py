import unittest


class Solution:
    def reformatNumber(self, number: str) -> str:

        def remove_spaces(number: str):
            number = number.replace(" ", "")
            number = number.replace("-", "")
            return number

        def add_dash(number: str):
            n = len(number)
            if n % 3 == 0:
                x = '-'.join(number[i:i + 3] for i in range(0, n, 3))
            elif n % 3 == 1:
                x = '-'.join(number[i:i + 3] for i in range(0, n, 3))
                x = list(x)
                x[-2], x[-3] = x[-3], x[-2]
                x = "".join(x)
            else:
                x = '-'.join(number[i:i + 3] for i in range(0, n, 3))
            return x

        x = remove_spaces(number)
        x = add_dash(x)
        return x



class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        number = "1-23-45 6"
        actual = solution.reformatNumber(number)
        expected = "123-456"
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        number = "123 4-567"
        actual = solution.reformatNumber(number)
        expected = "123-45-67"
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        number = "123 4-5678"
        expected = "123-456-78"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        number = "   1  2---"
        expected = "12"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        number = "12"
        expected = "12"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        number = "--17-5 229 35-39475 "
        expected = "175-229-353-94-75"
        actual = solution.reformatNumber(number)
        self.assertEqual(expected, actual)

