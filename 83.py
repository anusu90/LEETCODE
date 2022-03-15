# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, A: Optional[ListNode]) -> Optional[ListNode]:
        if A is None:
            return 
        if A.next is None:
            return A
        curr,node=A,A.next
        while node is not None:
            if curr.val==node.val:
                node=node.next
            else:
                curr.next=node
                curr=node
                node=node.next
        curr.next=node
        return A