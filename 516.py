class Solution:
    def longestPalindromeSubseq(self, A: str) -> int:
        n=len(A)
        dp=[[-1 for _ in range(n)] for _ in range(n)]

        def recurr(s,e):
            if s==e:
                dp[s][e]=1
            if s>e:
                dp[s][e]=0
            if dp[s][e]==-1:
                if A[s]==A[e]:
                    dp[s][e]=2 + recurr(s+1,e-1)
                else:
                    dp[s][e] = max(recurr(s+1,e),recurr(s,e-1))
            return dp[s][e]
        recurr(0,n-1)
        return dp[0][n-1]
        