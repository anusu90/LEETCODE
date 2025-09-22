class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = {}
        maxF=-1

        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
            
            maxF= max(maxF,f[i])
        
        sol=0

        for i in f:
            if f[i]==maxF:
                sol += f[i]

        return sol      