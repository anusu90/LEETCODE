class Solution:
    def findPeakGrid(self, grid: List[List[int]]) -> List[int]:
        s=0
        e=len(grid)-1
        while s<e:
            mid=(s+e)//2
            if max(grid[mid]) < max(grid[mid+1]):
                s=mid+1
            else:
                e=mid
        m=max(grid[s])
        j = grid[s].index(m)
        return [s,j]
        
