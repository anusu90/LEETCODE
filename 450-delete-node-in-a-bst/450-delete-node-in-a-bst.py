# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:     
        def recurr(root):
            if not root:
                return
            if root.val==key:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    temp = root.right
                    while temp.left:
                        temp=temp.left
                    root.val,temp.val=temp.val,root.val
                    root.right = recurr(root.right)
            if root.val>key:
                root.left=recurr(root.left)
            else:
                root.right=recurr(root.right)
            return root
        
        return recurr(root)
        