# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,curr):
            if root is None:
                return
            curr = (curr*10)+root.val
            left = dfs(root.left,curr)
            right = dfs(root.right,curr)
            if not left and not right:
                self.sol += curr
            return True
        sol = dfs(root,0)
        return self.sol
            
        
        