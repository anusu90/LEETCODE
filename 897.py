# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.sol=[]
    def recurr(self,root):
        if root is None:
            return
        self.recurr(root.left)
        self.sol.append(root.val)
        self.recurr(root.right)
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.recurr(root)
        n= len(self.sol)
        curr=r=TreeNode(self.sol[0])
        for i in range(1,n):
            curr.right = TreeNode(self.sol[i])
            curr=curr.right
        return r
            
            