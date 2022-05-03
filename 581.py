from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy = nums[:]
        copy.sort()
        n=len(nums)
        s,e,ptr=n-1,0,0
        flag=False
        while (ptr<n):
            if nums[ptr]!=copy[ptr]:
                flag=True
                s=min(s,ptr)
                e=max(e,ptr)
            ptr+=1
        if not flag:
            return 0
        return e-s+1