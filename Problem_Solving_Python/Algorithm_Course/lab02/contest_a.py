# lightoj 1004
# this problem doesn't support python
def calculate_bananas(diamond, dp, i, j, k):
    if diamond[i][j] == 0:
        return 0
    if i == k - 1:
        return diamond[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    bottom = diamond[i][j] + calculate_bananas(diamond, dp, i + 1, j, k)
    bottom_right = diamond[i][j] + calculate_bananas(diamond, dp, i + 1, j + 1, k)

    dp[i][j] = max(bottom, bottom_right)
    return dp[i][j]


def change_diamond(diamond, n):
    for i in range(n):
        zero_list = [0] * (n - i)
        diamond[i] += zero_list
    k = 2 * n - 1
    for i in range(n, k):
        diamond[i] += [0]
    for i in range(n, k):
        zero_list = [0] * (i - n + 1)
        diamond[i] = zero_list + diamond[i]


for case in range(int(input())):
    n = int(input())
    k = 2 * n - 1
    dp = [[-1] * (n + 1) for _ in range(k)]
    diamond = []
    for i in range(k):
        diamond.append(list(map(int, input().split())))
    change_diamond(diamond, n)
    # print(diamond)
    ans = calculate_bananas(diamond, dp, 0, 0, k)
    print("Case {}: {}".format(case + 1, ans))

# diamond = [
#     [7],
#     [6, 4],
#     [2, 5, 10],
#     [9, 8, 12, 2],
#     [2, 12, 7],
#     [8, 2],
#     [10]
# ]

# input
# 2
# 4
# 7
# 6 4
# 2 5 10
# 9 8 12 2
# 2 12 7
# 8 2
# 10
# 2
# 1
# 2 3
# 1
