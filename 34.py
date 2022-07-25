from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s1,s2,e1,e2=0,0,len(nums)-1,len(nums)-1
        l,r=-1,-1
        while(s1<=e1):
            mid = int((s1+e1)//2)
            if nums[mid]==target:
                l=mid
                e1=mid-1
            elif nums[mid]>target:
                e1=mid-1
            else:
                s1=mid+1
        while(s2<=e2):
            mid = (s2+e2)//2
            if nums[mid]==target:
                r=mid
                s2=mid+1
            elif nums[mid]>target:
                e2=mid-1
            else:
                s2=mid+1
        return [l,r]
        