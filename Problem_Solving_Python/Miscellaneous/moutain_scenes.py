# https://open.kattis.com/problems/scenes
# https://www.youtube.com/watch?v=pPgBZqY_Xh0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&index=4


def count_mountain_scenes(N, WIDTH, HEIGHT):
    MOD = 1_000_000_007
    ribbon_squares = min(HEIGHT * WIDTH, N)
    dp = [[-1] * (ribbon_squares + 1) for _ in range(WIDTH + 1)]  # -1 means null
    no_of_plains = ribbon_squares // WIDTH + 1

    def f(width, ribbon):
        if ribbon < 0:
            return 0
        if width > WIDTH:
            return 1
        if dp[width][ribbon] != -1:  # not null
            return dp[width][ribbon]
        count = 0
        for height in range(HEIGHT + 1):
            count += f(width + 1, ribbon - height)
        dp[width][ribbon] = count % MOD
        return dp[width][ribbon]

    ans = ((f(1, ribbon_squares) - no_of_plains) + MOD) % MOD
    return int(ans)