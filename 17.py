from typing import List


class Solution:
    def letterCombinations(self, A: str) -> List[str]:
        if len(A)==0:
            return []
        hashMap ={
            '0':'0',
            '1':'1',
            '2':"abc",
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        n=len(A)
        sol=[]
        def bt(curr,i,k):
            if i==n:
                t=curr[:]
                sol.append("".join(t))
                return
            st=hashMap[A[i]]
            m=len(st)
            for j in range(m):
                curr+=st[j]
                bt(curr,i+1,j)
                curr.pop()
        bt([],0,0)
        return sol
        