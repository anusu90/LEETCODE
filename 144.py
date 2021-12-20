# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.arr = []
    def re(self,n):
        if n is None:
            return
        self.arr.append(n.val)
        self.re(n.left)
        self.re(n.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.re(root)
        return self.arr
        