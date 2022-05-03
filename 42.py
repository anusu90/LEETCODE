from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        preFixMax=[]
        suffixMax=[]
        currMax=-1
        for i in range(1,n):
            currMax=max(currMax,height[i-1])
            preFixMax.append(currMax)
        j=n-1
        currMax=-1
        for j in range(n-2,-1,-1):
            currMax = max(currMax,height[j+1])
            suffixMax.append(currMax)
        water=0
        for i in range(1,n-1):
            h = min(preFixMax[i-1],suffixMax[n-2-i]) - height[i]
            if h>0:
                water+=h
        return water
        