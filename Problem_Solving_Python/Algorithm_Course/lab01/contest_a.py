# N = int(input())
# k = 2 * N - 1
# dp = [[-1]*N for _ in range(k)]
def calculate_bananas(a, dp, i, j, k):
    if a[i][j] == 0:
        return 0
    if i == k-1:
        return a[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    bottom = a[i][j] + calculate_bananas(a, dp, i+1, j, k)
    bottom_right = a[i][j] + calculate_bananas(a, dp, i+1, j+1, k)

    dp[i][j] = max(bottom, bottom_right)
    return dp[i][j]









# for i in range(N):
#     templist = list(map(int, input().split()))
#     length = len(templist)
#     for j in range(length):
#         a[i][j] = templist[j]
#

