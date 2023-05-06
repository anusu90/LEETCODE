class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        print(nums)
        mod = 10**9+7
        def binarySearch(index):
            end=n-1
            start=index
            sol=-1
            while start<=end:
                mid = (start+end)//2
                if nums[index]+nums[mid]==target:
                    sol=mid
                    start=mid+1
                elif nums[index]+nums[mid]>target:
                    end=mid-1
                elif nums[index]+nums[mid]<target:
                    sol=mid
                    start=mid+1
            return sol
        answer=0
        # print(binarySearch(2))
        for i in range(n):
            temp = binarySearch(i)
            tl = temp-i
            print(nums[i],"==>",i,"-to-",temp,"===",tl)
            if tl>=0:
                answer = (answer + pow(2, tl, mod)) % mod
        return answer
            
        