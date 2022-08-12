# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurr(node,p,q):
            if node is None:
                return None
            if node.val==p.val or node.val==q.val:
                return node
            l = recurr(node.left,p,q)
            r = recurr(node.right,p,q)
            if l and r:
                return node
            return l or r
        return recurr(root,p,q)
        