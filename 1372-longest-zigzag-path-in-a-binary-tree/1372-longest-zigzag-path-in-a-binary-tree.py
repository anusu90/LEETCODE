# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max=0
        def dfs(node,dist,direction):
            if node:
                self.max = max(self.max,dist)
                if direction == 'left':
                    dfs(node.right,dist+1,'right')
                    dfs(node.left,1,'left')
                elif direction =='right':
                    dfs(node.left,dist+1,'left')
                    dfs(node.right,1,'right')
        dfs(root,0,'left')
        dfs(root,0,'right')
        return self.max
        
        
        