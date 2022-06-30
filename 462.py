from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        i=0
        sol=0
        while(i<n//2):
            sol+= nums[n-1-i]-nums[i]
            i+=1
        return sol
            