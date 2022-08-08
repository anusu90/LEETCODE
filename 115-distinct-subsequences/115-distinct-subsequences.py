class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
        def recurr(la,lb):
            # print(la,lb)
            if lb==0:
                dp[la][lb]=1
            elif la==0:
                dp[la][lb]=0
            if dp[la][lb]==-1:
                if s[la-1]!=t[lb-1]:
                    dp[la][lb]=recurr(la-1,lb)
                else:
                    dp[la][lb]=recurr(la-1,lb-1)+recurr(la-1,lb)
            return dp[la][lb]
        sol = recurr(n,m)
        return sol
        