# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=fast=head
        while fast and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        prev,slow=slow,slow.next
        prev.next=None
        while slow:
            slow.next,prev,slow=prev,slow,slow.next
        slow,fast = head,prev
        while fast:
            if slow.val != fast.val:
                return False
            slow,fast=slow.next,fast.next
        return True
        
        
        
            
        