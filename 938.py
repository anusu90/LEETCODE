from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sumRange = 0
    def re(self,root,l,h):
        if root is None:
            return
        if root.val >= l and root.val <= h:
            self.sumRange += root.val
        self.re(root.left,l,h)
        self.re(root.right,l,h)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.re(root,low,high)
        return self.sumRange