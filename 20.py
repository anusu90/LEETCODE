class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2: return False
        stack=[]
        c=0
        for x in s:
            if x == "(" or x =="{" or x=="[":
                stack.append(x)
                c+=1
            else:
                if c<1:
                    return False
                else:
                    v=stack.pop()
                    c-=1
                    if x == ")" and v!="(":
                        return False
                    elif x=="}" and v!= "{":
                        return False
                    elif x=="]" and v!="[":
                        return False
        if c>0:
            return False
        return True
                