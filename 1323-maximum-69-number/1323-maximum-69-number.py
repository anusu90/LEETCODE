class Solution:
    def maximum69Number (self, num: int) -> int:
        digits=[]
        mod=10
        while num:
            digits.append(num%mod)
            num=num//mod
        
        n=len(digits)
        s,e=0,n-1
        
        while digits[e]!=6 and e>0:
            e-=1
            
        if digits[e]==6:
            digits[e]=9
            # digits[s]=6
        sol=0
        mult=1
        for x in digits:
            sol += x*mult
            mult *= 10
        return sol
        