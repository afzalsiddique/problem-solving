from math import sqrt


def is_prime_util(n, i, sq_root):
    if n == 1 or n == 2:
        return True
    if n == 4:
        return False
    if i == sq_root:
        return True
    if n % i:
        return is_prime_util(n, i + 1, sq_root)
    return False

def is_prime(n):
    return is_prime_util(n, 2, int(sqrt(n)) + 1)


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))
print(is_prime(11))
print(is_prime(12))
print(is_prime(13))