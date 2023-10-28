class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr2 = list(map(lambda x:x[::-1],arr))
        return " ".join(arr2)
        