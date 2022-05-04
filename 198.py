from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        sol = 0
        n=len(nums)
        dp=[-1]*(n+2)
        def recurr(start):
            if start>=n:
                dp[start]=0
            if dp[start]==-1:
                dp[start]=max(nums[start]+recurr(start+2),recurr(start+1))
            return dp[start]
        sol=recurr(0)
        return sol
        