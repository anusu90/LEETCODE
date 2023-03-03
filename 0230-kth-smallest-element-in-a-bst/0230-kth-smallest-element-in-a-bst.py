# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sol=None
        self.count=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recurr(root):
            global sol
            if root is None:
                return
            recurr(root.left)
            self.count+=1
            if self.count == k and self.sol is None:
                self.sol=root
            recurr(root.right)
            return
        recurr(root)
        if self.sol:
            return self.sol.val
        return -1
        