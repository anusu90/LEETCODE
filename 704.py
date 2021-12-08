from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        print(mid)
        while(start != end and nums[mid] != target and mid >= 0):
            print('here')
            if nums[mid] > target:
                end = mid - 1
            if nums[mid] < target:
                start = mid + 1
            mid = (start+end)//2
        if nums[mid] == target:
            return mid
        return -1


print(Solution().search([2, 5], 5))
