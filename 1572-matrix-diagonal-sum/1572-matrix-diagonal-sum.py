class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat[0])
        s=0
        for i in range(n):
            s+=mat[i][i]
            s+= mat[i][n-1-i]
        if n%2 != 0:
            k=(n-1)//2
            s -= mat[k][k]
        return s
        