# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def recurr(root):
            if not root:
                return
            recurr(root.left)
            self.arr.append(root.val)
            recurr(root.right)
        recurr(root)
        n=len(self.arr)
        curr=abs(self.arr[0]-self.arr[1])
        for i in range(2,n):
            curr = min(curr,abs(self.arr[i]-self.arr[i-1]))
        return curr
        

        