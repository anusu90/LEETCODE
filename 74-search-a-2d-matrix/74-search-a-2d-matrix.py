class Solution:
    def searchMatrix(self, A: List[List[int]], B: int) -> bool:
        row_start = 0
        row_end=len(A)-1
        mid=0
        while row_start<=row_end:
            mid = int((row_end+row_start)//2)
            if A[mid][-1]==B:
                return 1
            elif A[mid][-1]>B:
                if A[mid][0]==B:
                    return 1
                if A[mid][0]<B:
                    break
                row_end=mid-1
            else:
                row_start=mid+1
        
        row=mid

        s,e=0,len(A[0])-1

        while s<=e:
            mid = int((s+e)//2)
            if A[row][mid]==B:
                return 1
            elif A[row][mid]>B:
                e=mid-1
            else:
                s=mid+1
        
        return 0
        