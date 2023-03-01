class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        mid=(s+e)//2
        
        while s<e:
            mid=(s+e)//2
            if nums[mid]<nums[e]:
                e=mid
            else:
                s=mid+1
        print("here",s)
        if target<=nums[-1]:
            s=s
            e=len(nums)-1
        else:
            e=s-1
            s=0
            
        print("again",s,e)
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                e=mid-1
            else:
                s=mid+1
        return -1
                
        