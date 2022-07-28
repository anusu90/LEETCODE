class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        for x in s:
            if x not in hashMap:
                hashMap[x]=0
            hashMap[x]+=1
        
        for x in t:
            if x not in hashMap:
                return False
            hashMap[x]-=1
            if hashMap[x]==0:
                del hashMap[x]
        return len(hashMap)==0
        