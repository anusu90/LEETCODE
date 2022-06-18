from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        r=[1,-1,0,0]
        c=[0,0,1,-1]
        grid=[[0 for _ in range(cols)] for _ in range(rows)]
        while q:
            x,y = q.popleft()
            for k in range(4):
                dx, dy = x+r[k], y+c[k]
                if dx >= 0 and dx<rows and dy >= 0 and dy <cols and (dx, dy) not in visited:
                        matrix[dx][dy] = matrix[x][y] + 1
                        visited.add((dx, dy))
                        q.append((dx, dy))
        return matrix
