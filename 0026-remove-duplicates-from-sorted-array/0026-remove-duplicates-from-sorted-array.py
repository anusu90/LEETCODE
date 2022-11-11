class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(1,n):
            if nums[s]==nums[i]:
                continue
            else:
                s+=1
                if s!=i:
                    nums[s]=nums[i]
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                return i
        