class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashMap={}
        curr,sol=0,0
        i,j,n=0,0,len(nums)
        while(j<n):
            if nums[j] not in hashMap:
                hashMap[nums[j]]=1
                curr+=nums[j]
                j+=1
            else:
                while nums[j] in hashMap:
                    del hashMap[nums[i]]
                    curr -= nums[i]
                    i+=1
            sol=max(sol,curr)
        return sol
