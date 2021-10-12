def gcd(a,b):
    if b>a: return gcd(b,a)
    if b==0: return a
    return gcd(a-b,b)


def gcd2(a,b):
    if b>a: return gcd(b,a)
    if a%b==0: return b
    return gcd(b, a%b)
