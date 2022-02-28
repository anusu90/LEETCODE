class Solution:
    def findPairs(self, A: List[int], B: int) -> int:
        hashMap = {}
        count = 0
        if B==0:
            for x in A:
                if x in hashMap:
                    if hashMap[x]<2:
                        count+= hashMap[x]
                        hashMap[x]+=1
                else:
                    hashMap[x]=1
            return count
        for x in A:
            if x not in hashMap:
                hashMap[x]=1
        
        for x in A:
            if x+B in hashMap and hashMap[x]>0:
                count+=1
            if x-B in hashMap and hashMap[x]>0:
                count+=1
            hashMap[x]-=1
        return int(count/2)