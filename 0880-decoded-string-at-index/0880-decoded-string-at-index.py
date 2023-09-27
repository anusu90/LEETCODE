class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i in range(len(s)):
            if s[i].isdigit():
                size *= int(s[i])
            else:
                size += 1
        
        for i in range(len(s)-1,-1,-1):
            k = k%size
            if k==0 and s[i].isalpha():
                return s[i]

            if s[i].isdigit() :
                size = size/int(s[i])
                
            else:
                size -=1
        
        return ""
        
                
            
        