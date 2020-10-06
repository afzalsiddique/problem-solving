def gcd(small, big):
    if not big % small:
        return small
    return gcd(big % small, small)


print(gcd(3, 4))
print(gcd(9, 81))
print(gcd(3, 12))
print(gcd(10, 15))
