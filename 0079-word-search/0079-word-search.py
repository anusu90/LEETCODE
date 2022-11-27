class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        k=len(word)
        
        def dfs(r,c,l,visited):
            # print(r,c,l,visited)
            if l==k-1 and board[r][c]==word[l]:
                return True
            if l==k:
                return True
            if board[r][c]!=word[l]:
                return False
            visited[(r,c)]=True
            top=dfs(r-1,c,l+1,visited) if r-1>=0 and (r-1,c) not in visited else False
            bottom=dfs(r+1,c,l+1,visited) if r+1<n and (r+1,c) not in visited else False
            left=dfs(r,c-1,l+1,visited) if c-1>=0 and (r,c-1) not in visited else False
            right=dfs(r,c+1,l+1,visited) if c+1<m and (r,c+1) not in visited else False
            del visited[(r,c)]
            
            return top or bottom or left or right
        visited={}
        for i in range(n):
            for j in range(m):
                visited={}
                # print("i am called")
                found = dfs(i,j,0,visited)
                if found:
                    return True
        return False
        
        