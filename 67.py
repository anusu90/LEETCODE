class Solution:
    def addBinary(self, A: str, B: str) -> str:
        n = len(A)
        m = len(B)
        bEnd = m-1
        aEnd = n-1
        bit = 1
        sol = 0
        while(bEnd>=0 and aEnd>=0):
            s = int(A[aEnd])+int(B[bEnd])
            sol += s*bit
            bEnd -= 1
            aEnd -= 1
            bit = bit*2
        
        if(bEnd<0):
            while(aEnd>=0):
                s = int(A[aEnd])
                sol += s*bit
                bit = bit*2
                aEnd -= 1
        else:
            while(bEnd>=0):
                s = int(B[bEnd])
                sol += s*bit
                bit = bit*2
                bEnd -= 1
        return bin(sol)[2::]
        