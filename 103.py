# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, A: Optional[TreeNode]) -> List[List[int]]:
        if not A:
            return []
        sol=[]
        queue=[A]
        level=0
        while len(queue):
            level+=1
            temp=deque([])
            n=len(queue)
            for i in range(n):
                node = queue.pop(0)
                if level%2==0:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sol.append(list(temp))
        return sol
        