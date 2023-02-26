class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i]=i
        for i in range(m+1):
            dp[i][0]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[j][i]=dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j-1][i-1],dp[j][i-1],dp[j-1][i])+1
        return dp[-1][-1]
        
        