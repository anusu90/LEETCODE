from heapq import heappop,heappush
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        pq=[]
        for i in range(n-1):
            diff = heights[i+1]-heights[i]
            if diff>0:
                if ladders>0:
                    ladders-=1
                    heappush(pq,diff)
                elif len(pq)>0 and pq[0]<diff:
                    heappush(pq,diff)
                    replacement = heappop(pq)
                    bricks=bricks-replacement
                else:
                    bricks = bricks-diff
                if bricks<0:
                    return i
        return n-1
                
        
