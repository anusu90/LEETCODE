class Solution:
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        def recurr(k):
            if k==0:
                dp[k]=0
            if k==1:
                dp[k]=1
            if dp[k]==-1:
                dp[k]=recurr(k-1)+recurr(k-2)
            return dp[k]
        return recurr(n)