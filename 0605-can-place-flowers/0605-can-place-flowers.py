class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        i=0
        if m==1:
            return flowerbed[0]==0 or n==0
        while n and i<m:
            if flowerbed[i]==1:
                i+=1
                continue
            elif i==0 and flowerbed[i+1]==0:
                n-=1
                i+=2
            elif i==m-1 and flowerbed[i-1]==0:
                    n-=1
                    i+=2
            elif flowerbed[i-1] == 0 and flowerbed[i+1]==0:
                n-=1
                i+=2
            else:
                i+=1
        return n==0
                
        