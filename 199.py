# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol=[]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=[root]
        if not root:
            return []
        while len(queue)>0:
            n=len(queue)
            for i in range(n):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if i==n-1:
                    self.sol.append(curr.val)
        return self.sol
        
