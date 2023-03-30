from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashMap=defaultdict(int)
        n=len(nums)
        for x in nums:
            for y in x:
                hashMap[y]+=1
        sol=[]
        for k in hashMap:
            if hashMap[k]==n:
                sol.append(k)
        sol.sort()
        return sol
        
        
        