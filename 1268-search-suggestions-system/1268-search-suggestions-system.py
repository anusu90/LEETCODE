class TrieNode:
    def __init__(self,value):
        self.val=value
        self.hashMap={}
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        self.recommendation=[]
        
    def insert(self,word):
        curr=self.root
        for x in word:
            if x in curr.hashMap:
                curr=curr.hashMap[x]
            else:
                node = TrieNode(x)
                curr.hashMap[x]=node
                curr=curr.hashMap[x]
        curr.isEnd=True
        
    def dfs(self,node,word):
        if len(self.recommendation)==3:
            return
        if node.isEnd:
            self.recommendation.append(word)
        for x in "abcdefghijklmnopqrstuvwxyz":
            if x in node.hashMap:
                self.dfs(node.hashMap[x],word+x)
                
    def find(self,word):
        self.recommendation=[]
        curr=self.root
        for x in word:
            if x not in curr.hashMap:
                return self.recommendation
            else:
                curr=curr.hashMap[x]
        self.dfs(curr,word)
        return self.recommendation
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        sol=[]
        
        for x in products:
            trie.insert(x)
        prefix=""
        for x in searchWord:
            prefix += x
            temp = trie.find(prefix)
            # print(temp,prefix)
            sol.append(temp)
        return sol
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        