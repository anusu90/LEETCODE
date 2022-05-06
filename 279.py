class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        sqrs = [x * x for x in range(330)]
        for i in range(2, n + 1):
            dp[i] = i
            for x in sqrs:
                if x > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - x])
        return dp[n]