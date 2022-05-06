from functools import lru_cache


class Solution:

    def longestCommonSubsequenceMemo(self, text1: str, text2: str) -> int:
        return self.main(text1, text2, 0, 0)

    @lru_cache(maxsize=None)
    def main(self, text1: str, text2: str, i: int, j: int) -> int:
        if len(text1) == i or len(text2) == j:
            return 0
        if(text1[i] == text2[j]):
            return 1 + self.main(text1, text2, i+1, j+1)
        if(text1[i] != text2[j]):
            return max(self.main(text1, text2, i, j+1), self.main(text1, text2, i+1, j))

    def longestCommonSubsequenceTab(self, text1: str, text2: str) -> int:
        self.tab = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        print(self.tab)
        return self.mainTab(text1, text2, 0, 0)

    def mainTab(self, text1: str, text2: str, i: int, j: int) -> int:
        for row in range(0, len(text1)):
            for col in range(0, len(text2)):
                if(text1[row] == text2[col]):
                    self.tab[row+1][col+1] = self.tab[row][col] + 1
                if(text1[row] != text2[col]):
                    self.tab[row+1][col+1] = max(
                        self.tab[row+1][col], self.tab[row][col+1])
        print(self.tab)

        return self.tab[len(text1)][len(text2)]

# New solution using recurrsion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            n=len(text1)
            m=len(text2)
            dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
            def recurr(s1,s2,i,j,n,m):
                if dp[i][j]==-1:
                    if i==n or j==m:
                        dp[i][j]=0
                    elif s1[i]==s2[j]:
                        dp[i][j] = 1 + recurr(s1,s2,i+1,j+1,n,m)
                    else:
                        dp[i][j] = max(recurr(s1,s2,i+1,j,n,m),recurr(s1,s2,i,j+1,n,m))
                return dp[i][j]
            sol = recurr(text1,text2,0,0,n,m)
            return sol
