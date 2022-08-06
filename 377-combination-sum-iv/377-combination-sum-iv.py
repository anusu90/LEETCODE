class Solution:
    def __init__(self):
        self.count=0
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        
        for j in range(1,target+1):
            for i in range(1,n+1):
                if nums[i-1]<=j:
                    dp[i][j] = dp[i-1][j] + dp[n][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        