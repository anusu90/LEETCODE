# Definition for singly-linked list.
import heapq
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        head=curr=ListNode(0)
        n=len(lists)
        for i in range(n):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))
        while len(pq):
            val,idx,node = heapq.heappop(pq)
            curr.next = node
            curr=node
            if node.next:
                heapq.heappush(pq,(node.next.val,idx,node.next))
        return head.next