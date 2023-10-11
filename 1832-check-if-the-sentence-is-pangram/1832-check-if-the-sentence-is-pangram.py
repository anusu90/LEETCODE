class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = [False]*26
        for x in sentence:
            if x==" ":
                continue
            idx = ord(x)-97
            arr[idx]=True
        
        for x in arr:
            if not x:
                return False
        return True
        