class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(" ")[::-1]
        
        def filterIt(x):
            if x=="" or x==" ":
                return False
            return True
        a=filter(filterIt,a)
        return " ".join(a)
        