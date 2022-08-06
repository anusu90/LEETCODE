class Solution:
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
        