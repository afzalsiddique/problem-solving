# https://www.youtube.com/watch?v=cJ21moQpofY
def knapsack(capacity, WEIGHT, VALUE):
    N = len(WEIGHT)
    dp = [[0] * (capacity+1) for _ in range(N+1)]
    W, V = [0], [0]
    for i in range(N): # converting to 1 based indexing
        W.append(WEIGHT[i])
        V.append(VALUE[i])
    for i in range(1, N+1):
        for sz in range(1, capacity+1):
            weight, value = W[i], V[i]
            item_not_included = dp[i-1][sz]
            if sz >= weight and dp[i-1][sz-weight] + value > dp[i-1][sz]:
                item_included = dp[i-1][sz-weight] + value
            else:
                item_included = 0
            dp[i][sz] = max(item_included, item_not_included)

    items = []
    i, j = N, capacity
    while i != 0 and j != 0:
        if dp[i-1][j] != dp[i][j]:
            items.append(i)
            i, j = i - 1, j - W[i]
        else:
            i-=1


    return dp[N][capacity], items