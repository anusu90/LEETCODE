# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val==head.next.val
        s,f=head,head
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        
        curr=s.next
        prev=s
        
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        while head!=prev and head.next!=prev:
            print(head.val,prev.val)
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        if head.val!=prev.val:
            return False
        return True
        