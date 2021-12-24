class Solution:
    def isSubsequence(self, A: str, B: str) -> bool:
        na = len(A)
        nb = len(B)
        startPos = 0
        st=''
        for i in range(na):
            for k in range(startPos,nb):
                if A[i] == B[k]:
                    st += B[k]
                    startPos = k+1
                    break
                elif k==nb-1:
                    return False
        return st==A
        