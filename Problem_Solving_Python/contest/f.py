def calculate_b(a, new_b, b):
    return a*new_b + b
def get_b(a, b, n):
    if n==1:
        return b
    new_b = calculate_b(a, b, b)
    for i in range(2, n):
        new_b = calculate_b(a, new_b, b)
    return new_b

def get_a(a, n):
    return a**n


def fn(a,b,n):
    return get_a(a,n), get_b(a,b,n)

def f(a,b,n,m, MOD):
    new_a, new_b = fn(a,b,n)
    ans = 0
    for x in range(1,m+1):
        ans = ans + new_a * x + new_b
    return ans % MOD


for _ in range(int(input())):
    a,b,n,m,MOD = map(int, input().split())
    print(f(a,b,n,m,MOD))


# a,b,n,m, MOD = 2, 3, 1, 1, 100000000
# print(f(a,b,n,m,MOD))
# a,b,n,m, MOD = 2, 3, 1, 3, 100000000
# print(f(a,b,n,m,MOD))
# a,b,n,m, MOD = 1, 3, 1, 3, 100000000
# print(f(a,b,n,m,MOD))
# a,b,n,m, MOD = 2, 3, 2, 3, 100000000
# print(f(a,b,n,m,MOD))

