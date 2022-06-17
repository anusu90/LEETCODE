class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        e=n-1
        while s<e:
            mid=(s+e)//2
            if nums[mid]<nums[mid+1]:
                s=mid+1
            else:
                e=mid
        return e
