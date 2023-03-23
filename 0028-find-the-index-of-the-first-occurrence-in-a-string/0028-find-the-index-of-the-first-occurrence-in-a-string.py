class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m,n=len(haystack),len(needle)
        finalStr = needle+'$'+haystack
        print(finalStr)
        lps=[0]*(m+n+1)
        for i in range(1,m+n+1):
            x = lps[i-1]
            while finalStr[x]!=finalStr[i] and x>0:
                x = lps[x-1]
            if finalStr[x]==finalStr[i]:
                lps[i]=x+1
            if lps[i]==n:
                return i-(n*2)
        print(lps)
        return -1
            