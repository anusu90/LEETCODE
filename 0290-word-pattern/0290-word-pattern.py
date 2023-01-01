class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split(' ')
        n=len(arr)
        hash1={}
        hash2={}
        m=len(pattern)
        if n!=m:
            return False
        for i in range(n):
            if pattern[i] not in hash1 and arr[i] not in hash2:
                hash1[pattern[i]]=arr[i]
                hash2[arr[i]]=pattern[i]
            elif pattern[i] in hash1 and arr[i] not in hash2:
                return False
            elif pattern[i] not in hash1 and arr[i] in hash2:
                return False
            elif hash2[arr[i]] != pattern[i] or hash1[pattern[i]]!=arr[i]:
                return False
        return True
        