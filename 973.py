class Solution:
    def kClosest(self, A: List[List[int]], B: int) -> List[List[int]]:
        pq=[]
        sol=[]
        def calcD(p):
            [x,y]=p
            return x*x+y*y
        for point in A:
            distance = calcD(point)
            heapq.heappush(pq,(distance,point))
        sol=[]
        while B:
            p = heapq.heappop(pq)
            sol.append(p[1])
            B-=1
        return sol
        