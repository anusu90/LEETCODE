from typing import List


class Solution:
    def __init__(self):
        self.sol=True
    def isBipartite(self, B: List[List[int]]) -> bool:
        adj = {}
        visited={}
        for i in range(len(B)):
            adj[i]=B[i]
        # print('adj',adj)
        def dfs(node,parent,adj,visited):
            # print(visited)
            currColor = 1 if parent == None or parent == -1 else -1
            visited[node]= currColor
            for child in adj[node]:
                if child in visited:
                    if visited[child]==currColor:
                        # print("here",node,visited[child],parent)
                        self.sol=False
                else:
                    dfs(child,currColor,adj,visited)
            return True

        for k in adj:
            if k not in visited:
                dfs(k,None,adj,visited)
        return self.sol