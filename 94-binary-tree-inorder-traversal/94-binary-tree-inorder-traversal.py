# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recurr(node):
            if node is None:
                return
            recurr(node.left)
            self.sol.append(node.val)
            recurr(node.right)
        recurr(root)
        return self.sol
        