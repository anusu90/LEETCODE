# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, A, B: int, C: int):
        startPos=endPos=1
        n1=n2=A
        while startPos<B and n1.next:
            n1=n1.next
            startPos+=1
        while endPos<C and n2.next:
            n2=n2.next
            endPos+=1
        # print(startPos,endPos)
        if startPos==endPos:
            return A
        while startPos<endPos:
            temp=ListNode(n1.val)
            temp.next=n2.next
            n2.next=temp
            n1=n1.next
            startPos+=1
        n3=A
        startPos=1
        while startPos<B-1 and n3.next:
            n3=n3.next
            startPos+=1
        n3.next=n2
        if B==1:
            return n2
        return A