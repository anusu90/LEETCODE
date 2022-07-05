class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        sol=0
        for x in nums:
            if x-1 not in nums:
                y=x+1
                while y in nums:
                    y+=1
                sol=max(sol,y-x)
        return sol
