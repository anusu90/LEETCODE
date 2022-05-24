from heapq import nsmallest
from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols=len(grid[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        for i in range(cols):
            dp[0][i]=grid[0][i]
        for i in range(1,rows):
            for j in range(cols):
                [fs,ss]=nsmallest(2,dp[i-1])
                dp[i][j] = grid[i][j]+ (fs if dp[i-1].index(fs)!=j else ss)
        print(dp)
        return min(dp[-1])
            