class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = {}
        for x in s:
            if x not in hashMap:
                hashMap[x] = 0
            hashMap[x] += 1
        for y in t:
            if y not in hashMap:
                return y
            else:
                hashMap[y] -= 1
                if hashMap[y] == 0:
                    del hashMap[y]
        for x in hashMap:
            return x