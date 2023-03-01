# Definition for a binary tree node.
import sys
sys.setrecursionlimit(10**6)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n=len(nums)
        def recurr(s,e):
            if s>=n or e<0 or s>e:
                return None
            mid=(s+e)//2
            root = TreeNode(nums[mid])
            root.left = recurr(s,mid-1)
            root.right = recurr(mid+1,e)
            return root
        return recurr(0,n-1)
        