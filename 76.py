class Solution:
    def minWindow(self, A: str, B: str) -> str:
        n=len(A)
        hashB={}
        ans=""
        for x in B:
            if x not in hashB:
                hashB[x]=0
            hashB[x]+=1
        currCount = len(hashB)
        currWindow={}
        start,end=0,0
        for end in range(n):
            if A[end] in hashB:
                if A[end] not in currWindow:
                    currWindow[A[end]]=0
                currWindow[A[end]]+=1
                if currWindow[A[end]]==hashB[A[end]]:
                    currCount-=1
                if currCount==0:
                    if ans=="":
                        ans = A[start:end+1]
                    elif end-start<len(ans):
                        ans = A[start:end+1]
                    while(currCount==0):
                        if A[start] in hashB:
                            currWindow[A[start]] -=1
                            if currWindow[A[start]] >= hashB[A[start]]:
                                if end-start<len(ans):
                                    ans=A[start+1:end+1]
                            else:
                                currCount+=1
                        else:
                            if end-start<len(ans):
                                ans=A[start+1:end+1]
                        start+=1
        return ans
        

print(Solution().minWindow("ADOBECODEBANC","ABC"))