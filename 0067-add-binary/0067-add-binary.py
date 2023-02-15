class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=len(a)
        m=len(b)
        i=n-1
        j=m-1
        f=""
        while i>=0 and j>=0:
            f = str(int(a[i])+int(b[j]))+f
            i-=1
            j-=1
        
        while i>=0:
            f = a[i]+f
            i-=1
        
        while j>=0:
            f = b[j]+f
            j-=1
            
        s=""
        carry=0
        l=len(f)-1
        while l>=0:
            temp = int(f[l])+carry
            s = str(temp%2)+s
            carry = temp//2
            l-=1
        if carry:
            return str(carry)+s
        return s
        
        
        