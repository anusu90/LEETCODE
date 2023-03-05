class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSortedArray(arr1,arr2):
            n=len(arr1)
            m=len(arr2)
            final = [0]*(n+m)
            i,j,pos=0,0,0
            while i<n and j<m:
                if arr1[i]>arr2[j]:
                    final[pos]=arr2[j]
                    j+=1
                    pos +=1
                else:
                    final[pos]=arr1[i]
                    i+=1
                    pos +=1
            while i<n:
                final[pos]=arr1[i]
                i+=1
                pos +=1
            
            while j<m:
                final[pos]=arr2[j]
                j+=1
                pos +=1
            return final
        def recurr(s,e):
            if s==e:
                return [nums[s]]
            mid = (s+e)//2
            left = recurr(s,mid)
            right = recurr(mid+1,e)
            return mergeSortedArray(left,right)
        sol = recurr(0,len(nums)-1)
        print(sol)
        return sol
                    
            
        