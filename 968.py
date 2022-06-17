# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__ (self):
        self.sol=0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            val = dfs(node.left)+dfs(node.right)
            if val==0:
                return 3
            if val<3:
                return 0
            self.sol+=1
            return 1
        return self.sol+1 if dfs(root)>2 else self.sol
