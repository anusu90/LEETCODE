class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0,1]
        t = self.grayCode(A-1)
        return [x|(0<<(A-1)) for x in t] + [x|(1<<(A-1)) for x in t][::-1]