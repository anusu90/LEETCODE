from typing import List


class Solution:
    def generateMatrix(self, A: int) -> List[List[int]]:
        sol=[[0 for _ in range(A)] for _ in range(A)]

        rs=0
        re=A
        cs=0
        ce=A

        valToEnter=0

        while rs<re and cs<ce:
            for j in range(cs,ce):
                valToEnter+=1
                sol[rs][j]=valToEnter
            rs+=1
            for i in range(rs,re):
                valToEnter+=1
                sol[i][j]=valToEnter
            ce-=1
            for j in range(ce-1,cs-1,-1):
                valToEnter+=1
                sol[i][j]=valToEnter
            re-=1

            for i in range(re-1,rs-1,-1):
                valToEnter+=1
                sol[i][cs]=valToEnter
            cs+=1
        return sol
        