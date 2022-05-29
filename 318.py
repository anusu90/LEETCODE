from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        word_set = [set(words[i]) for i in range(n)]
        sol=0
        for i in range(n):
            for j in range(i+1,n):
                if not word_set[i] & word_set[j]:
                    sol=max(sol,len(words[i])*len(words[j]))
        return sol
        