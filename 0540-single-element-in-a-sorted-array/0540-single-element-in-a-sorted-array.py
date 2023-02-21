class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sol=0
        for x in nums:
            sol^=x
        return sol
        