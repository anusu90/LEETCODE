# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurr(node):
            if node is None:
                return (True,0)
            lb,ld=recurr(node.left)
            rb,rd=recurr(node.right)
            depth = max(ld,rd)+1
            if abs(ld-rd)>1 or lb==False or rb==False:
                return (False,depth)
            else:
                return (True,depth)
        sol,d=recurr(root)
        return sol