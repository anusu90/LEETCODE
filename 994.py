from typing import List


class Solution:
    def orangesRotting(self, A: List[List[int]]) -> int:
        r,c = len(A), len(A[0])
        sol=0
        queue=[]
        rows=[0,0,1,-1]
        cols = [1,-1,0,0]
        for i in range(r):
            for j in range(c):
                if A[i][j]==2:
                    queue.append([i,j])
        while len(queue)>0:
            n = len(queue)
            sol+=1
            for m in range(n):
                u,v=queue.pop(0)
                for k in range(4):
                    if u+rows[k]>=0 and u+rows[k]<r and v+cols[k]>=0 and v+cols[k]<c and A[u+rows[k]][v+cols[k]]==1:
                        A[u+rows[k]][v+cols[k]]=2
                        queue.append([u+rows[k],v+cols[k]])
        for i in range(r):
            for j in range(c):
                if A[i][j]==1:
                    return -1
        if sol==0:
            return 0
        return sol-1

        