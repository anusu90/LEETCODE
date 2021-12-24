class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 0
        initial = 1
        while (p<31 and initial<=n):
            if initial == n:
                return True
            p+=1
            initial = initial * 2
        return False
        