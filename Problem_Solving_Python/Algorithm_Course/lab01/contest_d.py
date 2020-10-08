def calculate_sum(triangle, n, dp, i, j):
    if i == n - 1:
        return triangle[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    bottom = triangle[i][j] + calculate_sum(triangle, n, dp, i + 1, j)
    bottom_right = triangle[i][j] + calculate_sum(triangle, n, dp, i + 1, j + 1)
    dp[i][j] = max(bottom, bottom_right)
    return dp[i][j]
for case in range(int(input())):
    triangle = []
    n = int(input())
    dp = [[-1] * n for _ in range(n)]
    for i in range(n):
        triangle.append(list(map(int, input().split())))
    print(calculate_sum(triangle, n, dp, 0, 0))
