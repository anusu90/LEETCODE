class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: 
            return 0
        parent = self.kthGrammar(n-1,k//2+k%2)
        if parent == 1:
            if k%2 == 0:
                return 0
            return 1
        elif parent ==0:
            if k%2 ==0:
                return 1
            return 0
        