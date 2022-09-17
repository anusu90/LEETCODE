# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashMap=defaultdict(int)
        def dfs(root):
            if root is None:
                return False
            if root.val in hashMap:
                return True
            hashMap[k-root.val]=1
            left = dfs(root.left)
            if left:
                return True
            return dfs(root.right)
        return dfs(root)
        