# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        hashMap={}
        for i in range(n):
            hashMap[inorder[i]]=i
        
        # a = pre order start
        # b = pre order end
        # x = in order start
        # y = in order end
        def createTree(a,b,x,y):
            if a>b or x>y:
                return None
            root = TreeNode(preorder[a])
            idx = hashMap[root.val]
            d = idx-x
            root.left = createTree(a+1,a+d,x,idx-1)
            root.right=createTree(a+d+1,b,idx+1,y)
            return root
        return createTree(0,n-1,0,n-1)
        