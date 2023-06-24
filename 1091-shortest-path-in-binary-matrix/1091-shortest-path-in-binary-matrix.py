class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        n=len(grid)
        visited={}
        dp = [ [-1 for i in range(n)] for k in range(n)]
        dp[0][0] = 1
        queue = [(0,0)]
        visited[(0,0)]=True
        while len(queue):
            x,y = queue.pop(0)
            curr = dp[x][y]
            arrPoints = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
            for l,m in arrPoints:
                if (l>=0 and l<n and m>=0 and m<n) and (l,m) not in visited and grid[l][m]==0:
                    visited[(l,m)]=True
                    queue.append((l,m))
                    dp[l][m] = curr+1
 
        return dp[-1][-1]
        
        