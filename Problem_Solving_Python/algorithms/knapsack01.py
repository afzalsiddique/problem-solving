# https://www.youtube.com/watch?v=cJ21moQpofY
def knapsack(capacity, W, V):
    N = len(W)
    dp = [[0] * (capacity+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for sz in range(1, capacity+1):
            weight, value = W[i-1], V[i-1]  # converting to 1 based indexing
            item_not_included = dp[i-1][sz]
            if sz >= weight and dp[i-1][sz-weight] + value > dp[i-1][sz]:
                item_included = dp[i-1][sz-weight] + value
            else:
                item_included = 0
            dp[i][sz] = max(item_included, item_not_included)

    return dp[N][capacity]