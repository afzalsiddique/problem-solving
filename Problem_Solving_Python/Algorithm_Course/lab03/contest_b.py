def lcs(a, b, m, n, dp):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


while True:
    try:
        a = input()
        b = input()
        m = len(a)
        n = len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        lcs(a, b, m, n, dp)
        # print(dp)

        path = []
        i, j = m, n
        while True:
            if i == 0 and j == 0:
                break
            if j == 0:
                path.append(a[i - 1])
                i -= 1
                continue
            if i == 0:
                path.append(b[j - 1])
                j -= 1
                continue
            if dp[i - 1][j] == dp[i][j]:
                path.append(a[i - 1])
                i -= 1
            elif dp[i][j - 1] == dp[i][j]:
                path.append(b[j - 1])
                j -= 1
            elif dp[i][j] > dp[i - 1][j - 1]:
                path.append(a[i - 1])
                i -= 1
                j -= 1
        print("".join(path[::-1]))
    except:
        break
