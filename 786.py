import heapq
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], B: int) -> List[int]:
        pq=[]
        n=len(A)
        for i in range(n):
            heapq.heappush(pq,(A[i]/A[n-1],i,n-1))
        while B>1:
            _,row,column = heapq.heappop(pq)
            column=column-1
            if column>0:
                heapq.heappush(pq,(A[row]/A[column],row,column))
            B-=1
        ans,row,column = heapq.heappop(pq)
        return [A[row],A[column]]
