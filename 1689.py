class Solution:
    def minPartitions(self, n: str) -> int:
        t=list(map(lambda x:int(x),n))
        return max(t)
