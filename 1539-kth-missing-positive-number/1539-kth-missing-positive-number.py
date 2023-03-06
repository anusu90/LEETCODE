class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pos=0
        i=1
        n=len(arr)
        while k>0 and pos<n:
            if i==arr[pos]:
                i+=1
                pos+=1
            else:
                k-=1
                i+=1
        i-=1
        return i+k
        
        