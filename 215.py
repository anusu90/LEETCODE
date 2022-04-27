from heapq import (heappop,heappush)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for x in nums:
            heappush(pq,-x)
        while k>1 and len(pq):
            heappop(pq)
            k-=1
        return -heappop(pq) 
        