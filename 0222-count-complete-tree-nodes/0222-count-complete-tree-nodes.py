# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.c=0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return
            self.c+=1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.c
        
        