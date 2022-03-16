# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, A: Optional[ListNode]) -> Optional[ListNode]:
        if not A:
            return
        slow=fast=A
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        if not fast.next or not fast.next.next:
            return None
        slow=A
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
        