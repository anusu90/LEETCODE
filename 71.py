class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        p = path.split("/")
        hashMap={
            "":1,
            ".":1,
            "..":1,
            "/":1
        }

        for x in p:
            if x not in hashMap:
                stack.append(x)
            elif x == ".." and len(stack)>0:
                stack.pop()
        if len(stack)==0:
            return "/"
        return "/" + "/".join(stack)
        