class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sol=[[0 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            sol[j][n-1]=1
        for i in range(n):
            sol[m-1][i]=1
        
        for k in range(m-2,-1,-1):
            for l in range(n-2,-1,-1):
                sol[k][l]=sol[k+1][l]+sol[k][l+1]
        return sol[0][0]