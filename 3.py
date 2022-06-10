class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        i,j=0,0
        sol=0
        hashMap={}
        while j<n:
            if s[j] not in hashMap:
                hashMap[s[j]]=1
                j+=1
                sol = max(sol,j-i)
            else:
                while s[j] in hashMap:
                    del hashMap[s[i]]
                    i+=1
        return sol