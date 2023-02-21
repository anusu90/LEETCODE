class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx=-1
        flag = False
        
        limit = min(list(map(lambda x:len(x),strs)))
        
        if len(strs)==1:
            return strs[0]
        for i in range(limit):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    flag=True
                    break
            if flag ==True:
                break
            else:
                print("here")
                idx=i
        
        return strs[0][:idx+1] if idx>=0 else ""
        