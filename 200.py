from typing import List


class Solution:
    def dfs(self,mat,i,j,visited,r,c):
        rows = [0,0,1,-1]
        cols = [1,-1,0,0]
        visited[i][j]=True
        for k in range(4):
            if i+rows[k]<r and i+rows[k]>=0 and j+cols[k]>=0 and j+cols[k]<c and visited[i+rows[k]][j+cols[k]]==False and mat[i+rows[k]][j+cols[k]]=='1':
                visited[i+rows[k]][j+cols[k]]=True
                self.dfs(mat,i+rows[k],j+cols[k],visited,r,c)
                
    def numIslands(self, A: List[List[str]]) -> int:
        r,c=len(A),len(A[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        count=0
        for i in range(r):
            for j in range(c):
                if visited[i][j]==False and A[i][j]=='1':
                    count+=1
                    self.dfs(A,i,j,visited,r,c)
        return count