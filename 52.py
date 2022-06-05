from typing import List


class Solution:
    def __init__(self):
        self.sol=0
    def totalNQueens(self, n: int) -> List[List[str]]:
        colMap={}
        diagMap1={}
        diagMap2={}
        def bt(curr,k,colMap,diagMap1,diagMap2):
            if k==n:
                temp = curr[:]
                self.sol+=1
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
        return self.sol
            
                    
                    
            
            
            
        