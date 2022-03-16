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