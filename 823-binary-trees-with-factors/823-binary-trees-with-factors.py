class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp={}
        MOD=1e9+7
        for x in arr:
            dp[x]=1
        
        for i,n in enumerate(arr):
            for j in range(i):
                if n%arr[j]==0 and n//arr[j] in dp:
                    dp[n]+=dp[arr[j]]*dp[n//arr[j]]
                    dp[n] %= MOD
        sol=0
        return int(sum(dp.values()) % MOD)
        