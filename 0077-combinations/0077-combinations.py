class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        def bt(idx,curr,temp):
            if curr == k:
                sol.append(temp[::])
            else:
                for t in range(idx,n+1):
                    temp.append(t)
                    bt(t+1,curr+1,temp)
                    temp.pop()
        bt(1,0,[])
        return sol
        
        
                
            