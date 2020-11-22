def summ(left, right):
    global arr
    ans = 0
    for i in range(left, right + 1):
        ans = (ans + arr[i]) % 100
    return ans


def rec(left, right):
    global dp, arr
    if left >= right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]
    dp[left][right] = float('inf')
    for breakk in range(left, right + 1):
        dp[left][right] = min(dp[left][right], rec(left, breakk) + rec(breakk + 1, right) + summ(left, breakk) * summ(breakk + 1, right))
    return dp[left][right]


while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [[-1] * (n + 1) for i in range(n + 1)]
        print(rec(0, n - 1))
    except:
        break
