class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs,re,cs,ce=0,len(matrix),0,len(matrix[0])
        sol=[]
        
        while rs<=re and cs<=ce:
            for i in range(cs,ce):
                if rs<re:
                    sol.append(matrix[rs][i])
            rs+=1
            for i in range(rs,re):
                if cs<ce:
                    sol.append(matrix[i][ce-1])
            ce-=1
            for i in range(ce-1,cs-1,-1):
                if rs<re:
                    sol.append(matrix[re-1][i])
            re-=1
            for i in range(re-1,rs-1,-1):
                if cs<ce:
                    sol.append(matrix[i][cs])
            cs+=1
            
        return sol
        