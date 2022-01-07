class Solution:
    def firstMissingPositive(self, nums):
        hashMap = {}
        n=len(nums)
        for x in nums:
            if x not in hashMap:
                hashMap[x]=1
        for i in range(1,n+2):
            if i not in hashMap:
                return i