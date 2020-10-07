def calculate_bananas(diamond, dp, i, j, k):
    if i == k - 1:
        return diamond[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    bottom_index = get_bottom1(i, j, n)
    if bottom_index[0] == None and bottom_index[1] == None:
        bottom =  0
    else:
        bottom = diamond[i][j] + calculate_bananas(diamond, dp, bottom_index[0], bottom_index[1], k)

    bottom_index = get_bottom2(i, j, n)
    if bottom_index[0] == None and bottom_index[1] == None:
        bottom_right = 0
    else:
        bottom_right = diamond[i][j] + calculate_bananas(diamond, dp, bottom_index[0], bottom_index[1], k)

    dp[i][j] = max(bottom, bottom_right)
    return dp[i][j]


def get_bottom1(i, j, n):
    if diamond[i][j] == diamond[i][-1]: # last column in the row
        return None, None
    return i + 1, j


def get_bottom2(i, j, n):
    if j == k-2:
        return None, None
    if i < n:
        return i + 1, j + 1
    return i + 1, j - 1


n = int(input())
k = 2 * n - 1
dp = [[-1] * (n + 1) for _ in range(k)]
diamond = []
for i in range(k):
    diamond.append(list(map(int, input().split())))
print(calculate_bananas(diamond, dp, 0, 0, k))

diamond = [
    [7],
    [6, 4],
    [2, 5, 10],
    [9, 8, 12, 2],
    [2, 12, 7],
    [8, 2],
    [10]
]


def change_diamond(diamond, n):
    for i in range(n):
        zero_list = [0] * (n - i)
        diamond[i] += zero_list
    k = 2 * n - 1
    for i in range(n, k):
        diamond[i] += [0]
    for i in range(n, k):
        zero_list = [0] * (i-n+1)
        diamond[i] = zero_list + diamond[i]

change_diamond(diamond, 4)
print(diamond)



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