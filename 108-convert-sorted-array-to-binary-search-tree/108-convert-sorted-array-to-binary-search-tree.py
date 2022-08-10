# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recurr(s,e):
            if s>e:
                return None
            mid= (s+e)//2
            node = TreeNode(nums[mid])
            node.left = recurr(s,mid-1)
            node.right = recurr(mid+1,e)
            return node
        
        n=len(nums)
        return recurr(0,n-1)
        