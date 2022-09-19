# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol=0
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        def recurr(root,maxVal):
            if not root:
                return
            if root.val >= maxVal:
                self.sol +=1
            currMax = max(maxVal,root.val)
            recurr(root.left,currMax)
            recurr(root.right,currMax)
            
        recurr(root,maxVal)
        
        return self.sol