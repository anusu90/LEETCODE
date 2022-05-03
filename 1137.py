class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        def recurr(k):
            if k<=0:
                dp[0]=0
            if k==1:
                dp[k]=1
            if k==2:
                dp[k]=1
            if dp[k]==-1:
                dp[k]=recurr(k-1)+recurr(k-2)+recurr(k-3)
            return dp[k]
        
        sol = recurr(n)
        return sol
        