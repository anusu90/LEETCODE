# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        nodeA=A
        nodeB=B
        head=curr=None
        carry=0
        while(nodeA and nodeB):
            val = (nodeA.val + nodeB.val+carry)%10
            carry =  (nodeA.val + nodeB.val+carry)//10
            if head is None:
                head=ListNode(val)
                curr=head
            else:
                node = ListNode(val)
                curr.next = node
                curr=curr.next
            nodeA=nodeA.next
            nodeB=nodeB.next
        
        while(nodeA):
            val = (nodeA.val+carry)%10
            carry =  (nodeA.val+carry)//10
            node = ListNode(val)
            curr.next = node
            curr=curr.next
            nodeA=nodeA.next

        while(nodeB):
            val = (nodeB.val+carry)%10
            carry =  (nodeB.val+carry)//10
            node = ListNode(val)
            curr.next = node
            curr=curr.next
            nodeB=nodeB.next
        if carry:
            node = ListNode(carry)
            curr.next = node


        return head
        