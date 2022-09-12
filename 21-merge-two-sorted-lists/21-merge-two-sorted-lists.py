# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s1=list1
        s2=list2
        curr=head=None
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while s1 and s2:
            if head is None:
                if s1.val<s2.val:
                    node = ListNode(s1.val)
                    curr = head = node
                    s1=s1.next
                else:
                    node = ListNode(s2.val)
                    curr = head = node
                    s2=s2.next
            else:
                if s1.val<s2.val:
                    node = ListNode(s1.val)
                    s1=s1.next
                else:
                    node = ListNode(s2.val)
                    s2=s2.next
                curr.next=node
                curr=curr.next
        while s1:
            node = ListNode(s1.val)
            s1=s1.next
            curr.next=node
            curr=curr.next
        while s2:
            node = ListNode(s2.val)
            s2=s2.next
            curr.next=node
            curr=curr.next

        return head
        