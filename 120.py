from typing import List


class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        level = len(A)
#         dp[i][j] represents the min sum path to go to the lowest level from the i,j cell in the triangle
        dp=[[-1 for _ in range (level+1)] for _ in range(level+1)]
        def recurr(i,j):
            if i>=level:
                dp[i][j]=0
            if dp[i][j]==-1:
                dp[i][j]=A[i][j] + min(recurr(i+1,j+1),recurr(i+1,j))
            return dp[i][j]
        recurr(0,0)
        return dp[0][0]