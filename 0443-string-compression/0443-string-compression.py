class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = None
        count=0
        sol_str=""
        for ch in chars:
            if curr == None or curr == ch:
                count+=1
            else:
                sol_str+=curr
                if count>1:
                    for x in str(count):
                        sol_str+=x
                count=1
            curr=ch
        sol_str+=curr
        if count>1:
            for x in str(count):
                sol_str+=x
        print(sol_str)
        for i,c in enumerate(sol_str):
            chars[i]=c
        return i+1
            
    
                
            
        