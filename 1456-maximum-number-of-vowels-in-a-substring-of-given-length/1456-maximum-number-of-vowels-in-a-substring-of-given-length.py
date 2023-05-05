from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a':True,'e':True,'i':True,'o':True,'u':True}
        n=0
        currentMap=defaultdict(int)
        for i in range(k):
            if s[i] in vowels:
                n+=1
            currentMap[s[i]]+=1
        sol=n
        i=k
        while i<len(s):
            if s[i] in vowels:
                n+=1
            if s[i-k] in vowels:
                n-=1
            sol=max(sol,n)
            i+=1
        return sol
        
                
        