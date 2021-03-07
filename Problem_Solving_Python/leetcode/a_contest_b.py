from math import sqrt


# class Solution:
#     def checkPowersOfThree(self, n: int) -> bool:
def checkPowersOfThree(n: int) -> bool:
    def cub_root(x: int) -> int:
        if x == 0 or x == 1: return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid * mid == x:
                return mid
            if mid * mid * mid <= x and (mid + 1) * (mid + 1) * (mid + 1) > x:
                return mid
            if mid * mid * mid > x:
                r = mid
            else:
                l = mid
        return mid

    def power(x, n):

        if (n == 0):
            return 1
        temp = power(x, n // 2)
        if (n % 2 == 0):
            return temp * temp
        else:
            return x * temp * temp

    def helper(n, start):
        if n == 0: return True
        if n < 0: return False
        root = cub_root(n)
        for i in range(start, root + 1):
            if helper(n - power(3, i), i + 1):
                return True
        return False

    return helper(n, 0)

# print(checkPowersOfThree(91))
# print(checkPowersOfThree(90))
# print(checkPowersOfThree(21))
# print(checkPowersOfThree(12))
# print(checkPowersOfThree(95224))
# print(checkPowersOfThree(2616799))
print(checkPowersOfThree(10000000))