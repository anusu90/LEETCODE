
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        queue=[root]
        while len(queue):
            n= len(queue)
            for i in range(n):
                curr=queue.pop(0)
                if curr is None:
                    continue
                if i==n-1:
                    curr.next=None
                else:
                    curr.next=queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root