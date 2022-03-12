# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev,curr=None,head
        temp=ListNode()
        while(curr is not None):
            temp.val,temp.next=curr.val,curr.next
            curr.next=prev
            prev=curr
            curr=temp.next
        return prev