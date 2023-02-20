class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        sol=0
        while s<=e:
            mid = (s+e)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                sol=mid+1
                s=mid+1
            else:
                e=mid-1
        return sol