from typing import List


class Solution:
    def combinationSum(self, A: List[int], B: int) -> List[List[int]]:
        curr=[]
        sol=[]
        n=len(A)
        def bt(curr,currSum,idx):
            if currSum>B:
                return
            if currSum==B:
                temp = curr[:]
                sol.append(temp)
                return
            for i in range(idx,n):
                currSum += A[i]
                curr.append(A[i])
                bt(curr,currSum,i)
                currSum-=curr[-1]
                curr.pop()
        bt(curr,0,0)
        return sol