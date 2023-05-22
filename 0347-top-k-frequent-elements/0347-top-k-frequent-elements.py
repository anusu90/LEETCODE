from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = defaultdict(int)
        for x in nums:
            hMap[x]+=1
        
        pq=[]
        for key in hMap:
            heappush(pq,(-1*hMap[key],key))
        sol=[]
        
        for i in range(k):
            _,v= heappop(pq)
            sol.append(v)
        return sol
            
        