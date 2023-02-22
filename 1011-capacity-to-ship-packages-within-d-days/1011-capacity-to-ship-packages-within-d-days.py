class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        def isPossible(w,d):
            curr=0
            for i in range(n):
                if curr + weights[i]>w:
                    d-=1
                    curr=weights[i]
                else:
                    curr += weights[i]
                if d==0:
                    return False
            return True
    
        s=max(weights)
        e=sum(weights)
        sol=-1
    
        
        while s<=e:
            mid = (s+e)//2
            print(mid)
            if isPossible(mid,days):
                sol=mid
                e=mid-1
            else:
                s=mid+1
        return sol