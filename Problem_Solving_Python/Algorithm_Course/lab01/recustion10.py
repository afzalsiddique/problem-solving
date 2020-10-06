def lcm_util(small, big, x):
    if big * x % small == 0:
        return big * x
    else:
        return lcm_util(small, big, x + 1)


def lcm(small, big):
    return lcm_util(small, big, 1)


print(lcm(4, 6))
print(lcm(6, 18))
