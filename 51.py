from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colMap={}
        diagMap1={}
        diagMap2={}
        sol=[]
        def bt(curr,k,colMap,diagMap1,diagMap2):
            if k==n:
                temp = curr[:]
                sol.append(temp)
                return
            for c in range(n):
                if c not in colMap and (k-c) not in diagMap1 and k+c not in diagMap2:
                    curr.append([k,c])
                    colMap[c]=1
                    diagMap1[(k-c)]=1
                    diagMap2[k+c]=1
                    bt(curr,k+1,colMap,diagMap1,diagMap2)
                    curr.pop()
                    del colMap[c]
                    del diagMap1[(k-c)]
                    del diagMap2[k+c]
        bt([],0,colMap,diagMap1,diagMap2)
        ans=[]
        for l in range(len(sol)):
            temp=[]
            for k in range(len(sol[l])):
                q=""
                for m in range(n):
                    if m==sol[l][k][1]:
                        q+='Q'
                    else:
                        q+='.'
                temp.append(q)
            ans.append(temp)
        return ans
            
                    
                    
            
            
            
        