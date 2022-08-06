class Solution:
    def __init__(self):
        self.count=0
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp=[0 for _ in range(target+1)]
        
        dp[0]=1
        
        for j in range(1,target+1):
            for i in range(1,n+1):
                if nums[i-1]<=j:
                    dp[j] += dp[j-nums[i-1]]
        return dp[-1]
        