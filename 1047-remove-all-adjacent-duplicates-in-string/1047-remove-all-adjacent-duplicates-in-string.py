class Solution:
    def removeDuplicates(self, A: str) -> str:
        stack=[]
        for x in A:
            shouldInsert=True
            while len(stack)>0 and stack[-1]==x:
                stack.pop()
                shouldInsert=False
            if shouldInsert:
                stack.append(x)
        return "".join(stack)
        