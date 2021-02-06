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


