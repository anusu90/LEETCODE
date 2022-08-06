class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        
        
        for j in range(1,target+1):
            for i in range(1,n+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-nums[i-1]] if j>=nums[i-1] else dp[i-1][j]
                # print(dp)
        return dp[-1][-1]
        