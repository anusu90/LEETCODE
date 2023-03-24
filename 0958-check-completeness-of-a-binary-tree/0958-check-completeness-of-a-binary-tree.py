# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        found_none=False
        while len(queue):
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if found_none and (node.left or node.right):
                    return False
                if node.right and not node.left:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.right or not node.left:
                    found_none=True
        return True
        