from collections import deque

class Solution:
    def maxSlidingWindow(self, A: List[int], B: int) -> List[int]:
        dq = deque([])
        for i in range(B):
            while len(dq) and dq[-1]<A[i]:
                dq.pop()
            dq.append(A[i])
        sol = [dq[0]]
        currMax = dq[0]
        for i in range(B,len(A)):
            out = A[i-B]
            coming = A[i]
            if out == dq[0]:
                dq.popleft()
            while len(dq) and dq[-1]<A[i]:
                dq.pop()
            dq.append(A[i])
            sol.append(dq[0])
        return sol
