from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        limit = pow(2,n)
        sol = []
        for i in range(limit):
            temp = []
            for j in range(n):
                if (i>>j)&1 == 1:
                    temp.append(nums[j])
            sol.append(temp)
        return sol
        