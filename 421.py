from typing import List


class TrieNode:
    def __init__(self):
        self.map={}
        self.isEnd=False
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=curr=TrieNode()
        sol=0
        for x in nums:
            curr=root
            for i in range(31,-1,-1):
                val =(x>>i) & 1
                if val in curr.map:
                    curr=curr.map[val]
                else:
                    node = TrieNode()
                    curr.map[val]=node
                    curr=node
            curr.isEnd=True
        for x in nums:
            curr=root
            currXor=None
            for i in range(31,-1,-1):
                val=(x>>i) & 1 
                rev = val ^ 1
                # print(x,val,rev)
                if rev in curr.map:
                    if currXor:
                        currXor=currXor<<1
                        currXor|=1
                    else:
                        currXor=1
                    curr=curr.map[rev]
                else:
                    if currXor:
                        currXor=currXor<<1
                    else:
                        currXor=0
                    curr=curr.map[val]
            print(currXor,x)
            sol=max(sol,currXor)
        return sol
                
        
                
        