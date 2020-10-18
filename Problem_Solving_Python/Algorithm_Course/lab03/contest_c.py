def change(amount, coins, m) -> int:
    dp = [[0] * (amount + 1) for _ in range(m + 1)]
    for row in dp:
        row[0] = 1
    for i in range(1, m + 1):
        for j in range(1, amount + 1):
            if j >= coins[i - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][amount]


amount, m = map(int, input().split())
coins = list(map(int, input().split()))
print(change(amount,coins,m))