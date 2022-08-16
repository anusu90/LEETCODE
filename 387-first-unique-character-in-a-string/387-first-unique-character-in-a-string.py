class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap={}
        for x in s:
            if x not in hashMap:
                hashMap[x]=0
            hashMap[x] += 1
        for i in range(len(s)):
            if hashMap[s[i]]==1:
                return i
        return -1
        