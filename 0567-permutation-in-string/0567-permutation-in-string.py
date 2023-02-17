from collections import defaultdict
class Solution:
    def compareObj(self,obj1,obj2):
        print(obj1,obj2)
        for x in range(26):
            if obj1[x]!=obj2[x]:
                return False
        return True
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapOne=[0]*26
        mapTwo=[0]*26
        n=len(s1)
        m=len(s2)
        if m<n:
            return False
        for x in s1:
            mapOne[ord(x)-97]+=1
        for x in range(n):
            mapTwo[ord(s2[x])-97]+=1
        if self.compareObj(mapOne,mapTwo):
            return True
        for i in range(n,m):
            mapTwo[ord(s2[i])-97]+=1
            mapTwo[ord(s2[i-n])-97]-=1
            if self.compareObj(mapOne,mapTwo):
                return True
        return False
        
        