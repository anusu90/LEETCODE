class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap={}
        
        while n not in hashMap and n != 1:
            # print(n)
            hashMap[n]=True
            t1=n
            t2=0
            while t1>0:
                t2 += (t1%10)**2
                t1=t1//10
            n=t2
        return n==1
        