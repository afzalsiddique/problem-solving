def calculate_bananas(a, dp, i, j, k):
    if a[i][j] == 0:
        return 0
    if i == k - 1:
        return a[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    bottom = a[i][j] + calculate_bananas(a, dp, i + 1, j, k)
    bottom_right = a[i][j] + calculate_bananas(a, dp, i + 1, j + 1, k)

    dp[i][j] = max(bottom, bottom_right)
    return dp[i][j]


n = int(input())
k = 2 * n - 1
dp = [[-1] * (n+1) for _ in range(k)]
a = [[0] * (n+1) for _ in range(k)]



for i in range(n):
    templist = list(map(int, input().split()))
    tempListlenght = len(templist)
    for j in range(n+1):
        if j < tempListlenght:
            a[i][j] = templist[j]
print(a)
for i in range(n, 2*n-1):
    templist = list(map(int, input().split()))
    for j in range(n+1):
        if j < i-n+1 or j >= 2*n-1:
            continue
        a[i][j] = templist[j]
print("\n\n")
print(a)
    # for j in range(i-n+1, 2*n-1):

