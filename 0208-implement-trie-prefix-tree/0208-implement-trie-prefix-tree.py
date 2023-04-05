class TrieNode:
    def __init__(self,c):
        self.char=c
        self.charArray=[-1]*26
        self.isEnd=False
        
    def markEnd(self):
        self.isEnd=True

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            idx_c = ord(c)-97
            if curr.charArray[idx_c]==-1:
                new_node=TrieNode(c)
                curr.charArray[idx_c]=new_node
            curr=curr.charArray[idx_c]
        curr.markEnd()
    
    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            idx_c = ord(c)-97
            if curr.charArray[idx_c]==-1:
                return False
            else:
                curr=curr.charArray[idx_c]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            idx_c = ord(c)-97
            if curr.charArray[idx_c]==-1:
                return False
            else:
                curr=curr.charArray[idx_c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)