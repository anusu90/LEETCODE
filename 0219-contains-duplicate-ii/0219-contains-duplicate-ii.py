class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap={}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hmap:
                hmap[nums[i]]=i
            else:
                if abs(i-hmap[nums[i]])<=k:
                    return True
                else:
                    hmap[nums[i]]=i
        return False
        
        