class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suff=[1]*n
        
        pre[0]=nums[0]
        suff[-1]=nums[-1]
        
        sol=[0]*n
        
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i]
        
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]*nums[i]
            
        for i in range(n):
            sol[i] = (pre[i-1] if i>0 else 1)*(suff[i+1] if i+1<n else 1)
        return sol
            
        
        