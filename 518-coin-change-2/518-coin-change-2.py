class Solution:
    def change_tabulation(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(target+1)]
        
        dp[0]=1
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    dp[j] += dp[j-nums[i-1]]
        return dp[-1]
    
    def change(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(target+1)] for _ in range(n+1)]
        
        def recurr(n,k):
            if k==0:
                dp[n][k]=1
            elif n==0:
                dp[n][k]=0
            if dp[n][k]==-1:
                dp[n][k] = recurr(n-1,k) + (0 if nums[n-1]>k else recurr(n,k-nums[n-1]))
            return dp[n][k]
        
        return recurr(n,target)
        
        