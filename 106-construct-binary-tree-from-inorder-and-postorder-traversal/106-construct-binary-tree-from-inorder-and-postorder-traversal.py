# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        hashMap={}
        for i in range(n):
            hashMap[inorder[i]]=i
		
		# a = inorder start
		# b = inorder end
		# x = postorder start
		# y = postorder end
        def createTree(a,b,x,y):
            if a>b or x>y:
                return None
            root = TreeNode(postorder[y])
            idx = hashMap[root.val]
            element_on_right = b-idx
            element_on_left  = idx-a
            root.left = createTree(a,idx-1,x,x+element_on_left-1)
            root.right = createTree(idx+1,b,y-element_on_right,y-1)
            return root
        
        return createTree(0,n-1,0,n-1)
        