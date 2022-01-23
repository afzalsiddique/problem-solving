# see leetcode 187
# https://leetcode.com/problems/longest-common-subpath/discuss/1314316/Python-2-solutions%3A-Rolling-Hash-and-Suffix-Array-explained.
def RabinKarp(arr, M, q): # M=window size
    h, t, d = (1<<(17*M-17))%q, 0, 1<<17
    all_hashes = set()

    for i in range(M):
        t = (d * t + arr[i])% q

    all_hashes.add(t)

    for i in range(len(arr) - M):
        t = (d*(t-arr[i]*h) + arr[i + M])% q
        all_hashes.add(t)

    return all_hashes
