from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        state = [True]*10
        sol=[]
        l=len(nums)
        def bt(curr,state,index,count,balance):
            if balance<0:
                return
            if count==k:
                if balance==0:
                    temp=curr[:]
                    sol.append(temp)
                    return
                else:
                    return
            for i in range(index,l):
                if state[i]:
                    curr.append(nums[i])
                    state[i]=False
                    bt(curr,state,i+1,count+1,balance-nums[i])
                    curr.pop()
                    state[i]=True
        bt([],state,0,0,n)
        return sol