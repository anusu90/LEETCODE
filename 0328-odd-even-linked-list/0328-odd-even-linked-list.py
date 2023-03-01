# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp=head.next
        if temp is None:
            return head
        prev=head
        curr=temp
        count=0
        while curr and curr.next:
            print(curr.val)
            count+=1
            prev.next=curr.next
            prev=curr
            curr=curr.next
        
        if count%2==0:
            prev.next=temp
            curr.next=None
        else:
            prev.next=None
            curr.next=temp
        return head
        
        