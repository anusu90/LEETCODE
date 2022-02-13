from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []
        for x in range(n+1):
            t=0
            for i in range(32):
                t+=(x>>i)&1
            sol.append(t)
        return sol