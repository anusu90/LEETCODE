class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        rs,re,cs,ce=0,len(matrix),0,len(matrix[0])
        sol=[]
        while rs<re and cs<ce:
            temp=[]
            for i in range(cs,ce):
                sol.append(matrix[rs][i])
            rs+=1
            for i in range(rs,re):
                sol.append(matrix[i][ce-1])
            ce-=1
            for i in range(ce-1,cs-1,-1):
                sol.append(matrix[re-1][i])
            re-=1
            for i in range(re-1,rs-1,-1):
                sol.append(matrix[i][cs])
            cs+=1
        return sol[:m*n]
                
        