# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue=[]
        hashMap={target:True}
        def assignParent(node,parent=None):
            if(node):
                node.parent=parent
                assignParent(node.left,node)
                assignParent(node.right,node)
        assignParent(root)
        level=0
        queue=[target]
        while(len(queue)>0):
            if level==k:
                break
            n=len(queue)
            for i in range(n):
                curr=queue.pop(0)
                if curr.parent and curr.parent not in hashMap:
                    queue.append(curr.parent)
                    hashMap[curr.parent]=True
                if curr.left and curr.left not in hashMap:
                    queue.append(curr.left)
                    hashMap[curr.left]=True
                if curr.right and curr.right not in hashMap:
                    queue.append(curr.right)
                    hashMap[curr.right]=True
            level+=1
        sol=[]
        for x in queue:
            sol.append(x.val)
        return sol