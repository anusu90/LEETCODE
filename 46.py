from typing import List


class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        n=len(A)
        curr=[]
        sol=[]
        state=[False]*n
        def bt(curr,state):
            if len(curr)==n:
                sol.append(curr[:])
                return
            for i in range(n):
                if state[i]:
                    continue
                curr.append(A[i])
                state[i]=True    
                bt(curr,state)
                curr.pop()
                state[i]=False
        bt(curr,state)
        return sol
        