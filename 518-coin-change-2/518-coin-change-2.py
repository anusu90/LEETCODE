class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(target+1)]
        
        dp[0]=1
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    dp[j] += dp[j-nums[i-1]]
        return dp[-1]
        