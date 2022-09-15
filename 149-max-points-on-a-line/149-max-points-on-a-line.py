class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        n=len(A)
        sol=0
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(n):
            hashMap={}
            sameLine=0
            for j in range(i+1,n):
                [x1,y1]=[A[i][0],A[i][1]]
                [x2,y2]=[A[j][0],A[j][1]]
                dx,dy=x2-x1,y2-y1
                # print(dy,dx)
                if dx==0 and dy==0:
                    sameLine+=1
                elif dy==0:
                    m,c=0,0
                elif dx==0:
                    m,c=float('inf'),float('inf')
                else:
                    gcd=math.gcd(dy,dx)
                    m,c=int(dy/gcd),int(dx/gcd)
                    if m*c <0:
                        if c<0:
                            m,c=-m,-c
                    if m*c >0:
                        if c<0:
                            m,c=-m,-c
                if (m,c) not in hashMap:
                    hashMap[(m,c)]=1
                hashMap[(m,c)]+=1
            for k in hashMap.values():
                sol=max(sol,k+sameLine)
        return sol
        