from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue=deque()
        dQueue=deque()
        n=len(senate)
        
        for i,x in enumerate(senate):
            if x=='R':
                rQueue.append(i)
            else:
                dQueue.append(i)
        
        while rQueue and dQueue:
            r=rQueue.popleft()
            d=dQueue.popleft()
            
            if d>r:
                rQueue.append(n+r)
            else:
                dQueue.append(n+d)
                
        return 'Radiant' if rQueue else "Dire"
        