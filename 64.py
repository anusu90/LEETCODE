from typing import List


class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        rows=len(A)
        cols=len(A[0])
        dp =[[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0]=A[0][0]
        for i in range(1,cols):
            dp[0][i]=A[0][i]+dp[0][i-1]
        for i in range(1,rows):
            dp[i][0]=A[i][0]+dp[i-1][0]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = A[i][j] + min(dp[i][j-1],dp[i-1][j])
        return dp[rows-1][cols-1]
        