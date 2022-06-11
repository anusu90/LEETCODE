class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m=len(s)
        rev=s[::-1]
        new_s = s+'*'+rev
        n=len(new_s)
        lps=[0]*(n)
        for i in range(1,n):
            x=lps[i-1]
            while x>0 and new_s[x]!=new_s[i]:
                x=lps[x-1]
            if new_s[x]==new_s[i]:
                x+=1
            lps[i]=x
        k=lps[-1]
        return s[k:m][::-1]+s