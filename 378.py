from heapq import heappop,heappush
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq=[]
        r,c=len(matrix),len(matrix[0])
        for i in range(r):
            for j in range(c):
                heappush(pq,matrix[i][j])
        while k>1:
            heappop(pq)
            k-=1
        return pq[0]
        