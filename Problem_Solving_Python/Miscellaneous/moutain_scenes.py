# https://open.kattis.com/problems/scenes


class Solution:
    def count_mountain_scenes(self, ribbon, WIDTH, HEIGHT):
        MOD = 1_000_000_007
        dp = [[-1] * (ribbon + 1) for _ in range(WIDTH + 1)]  # -1 means null
        ribbon = min(HEIGHT * WIDTH, ribbon)
        no_of_plains = ribbon // WIDTH + 1

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
            dp[width][ribbon] = count
            return dp[width][ribbon] % MOD

        ans = ((f(1, ribbon) - no_of_plains) + MOD) % MOD
        return int(ans)