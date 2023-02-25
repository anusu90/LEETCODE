class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        currMax=0
        maxProfit=0
        for i in range(n-1,-1,-1):
            if prices[i]>currMax:
                currMax=prices[i]
            maxProfit = max(maxProfit,currMax-prices[i])
        return maxProfit
            
        