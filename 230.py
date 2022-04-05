# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
        self.ans=0
    def recc(self,A,B):
        if A is None:
            return
        self.recc(A.left,B)
        self.count+=1
        if self.count==B:
            self.sol = A.val
        else:
            self.recc(A.right,B)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.recc(root,k)
        return self.sol
        