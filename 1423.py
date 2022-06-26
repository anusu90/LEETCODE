class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        select=n-k
        total=0
        for x in cardPoints:
            total+=x
        if select==0:
            return total
        curr=0
        for i in range(select):
            curr += cardPoints[i]
        sol=curr
        for i in range(select,n):
            curr = curr - cardPoints[i-select]+cardPoints[i]
            sol=min(sol,curr)
        return total-sol
        
