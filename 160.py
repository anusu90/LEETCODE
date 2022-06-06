from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA,headB):
        currA=headA
        currB=headB
        hashA={}
        while currA is not None:
            hashA[currA]=True
            currA=currA.next
        while currB is not None:
            if currB in hashA:
                return currB
            currB=currB.next
        return None

# O(1) solution for the same question
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA,currB=headA,headB
        lenA,lenB=0,0
        while currA is not None:
            lenA+=1
            currA=currA.next
        while currB is not None:
            lenB+=1
            currB=currB.next
        currA,currB=headA,headB
        if lenA>lenB:
            while lenA>lenB:
                currA=currA.next
                lenA-=1
        else:
            while lenB>lenA:
                currB=currB.next
                lenB-=1
        while currA is not None and currB is not None:
            if currA==currB:
                return currA
            else:
                currA=currA.next
                currB=currB.next
        return None