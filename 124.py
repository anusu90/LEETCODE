# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.sol=-10e9
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recurr(node):
            if node is None:
                return 0
            l=recurr(node.left)
            r=recurr(node.right)
            val=max(node.val,node.val+l,node.val+r)
            self.sol=max(val,self.sol,node.val+r+l)
            return val
        recurr(root)
        return self.sol