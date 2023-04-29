# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width=0
        dq = deque([(root,0)])
        while len(dq):
            width = max(width,dq[-1][1]-dq[0][1])
            for _ in range(len(dq)):
                node,idx = dq.popleft()
                if node.left:
                    dq.append((node.left,2*idx))
                if node.right:
                    dq.append((node.right,2*idx+1))
            
        return width+1
        
                    
        