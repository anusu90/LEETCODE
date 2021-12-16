from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0: 1}
        prev = 0
        count = 0
        for r in nums:
            prev += r
            need = prev - k
            if need in hashMap:
                count += hashMap[need]
            if prev in hashMap:
                hashMap[prev] += 1
            else:
                hashMap[prev] = 1
        return count


n = [3, 4, 7, 2, -3, 1, 4, 2]
print(Solution().subarraySum(n, 7))
