class Solution:
    def divide(self, A: int, B: int) -> int:
        if (A == -2147483648 and B == -1): return 2147483647
        positive = (A < 0) is (B < 0)
        if B==1:
            return A
        a,b,ans=abs(A),abs(B),0
        while a>=b:
            bitCount=0
            while a>(b<<(bitCount+1)):
                bitCount+=1
            ans+=(1<<bitCount)
            a -= (b<<bitCount)
        return ans if positive else -ans