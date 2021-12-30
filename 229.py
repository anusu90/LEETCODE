class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        if n==2:
            if nums[0]==nums[1]:
                return [nums[0]]
            return nums
        me1,f1,me2,f2=None,0,None,0
        for i in range(n):
            if me1 is None and nums[i]!=me2:
                me1 = nums[i]
                f1+=1
            elif me1 == nums[i]:
                f1+=1
            elif me2 is None:
                me2= nums[i]
                f2+=1
            elif me2 == nums[i]:
                f2+=1
            else:
                f2-=1
                f1-=1
                if f1==0:
                    me1 = None
                if f2==0:
                    me2=None
        sol,f1,f2=[],0,0
        for x in nums:
            if x==me1:
                f1+=1
            elif x==me2:
                f2+=1
        if f1>n/3:
            sol.append(me1)
        if f2>n/3 and me2!=me1:
            sol.append(me2)
        return sol