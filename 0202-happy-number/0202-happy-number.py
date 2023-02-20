class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap={}
        while n!=1 and n not in hashMap:
            hashMap[n]=True
            k=0
            while n>0:
                r=n%10
                n=n//10
                k=k+(r*r)
            # print(k)
            n=k
        return n==1
        