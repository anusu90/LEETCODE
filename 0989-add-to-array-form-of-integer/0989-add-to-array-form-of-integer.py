class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=len(num)
        i=10
        c=1
        s=0
        for i in range(n):
            s=(s*10+num[i])
        new=s+k
        arr=[]
        while new>0:
            d = new%10
            new = new//10
            arr.append(d)
        return arr[::-1]
            
        