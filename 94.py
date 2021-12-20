# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def re (self,root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.arr.append(root.val)
        self.inorderTraversal(root.right)

    def inorderTraversal(self, A: Optional[TreeNode]) -> List[int]:
        self.re(A)
        return self.arr