# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dq=deque([])
        sol=[]
        dq.append(root)
        level=0
        while len(dq):
            n=len(dq)
            temp=deque([])
            for i in range(n):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                if level%2==0:
                    temp.append(node.val)
                if level%2!=0:
                    temp.appendleft(node.val)
            level+=1
            sol.append(temp)
        return sol
                    
                    
                
        
        