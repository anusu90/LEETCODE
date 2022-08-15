class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            "M":1000
        }
        test={
            "I":1,
            'X':1,
            "C":1
        }
        sol=0
        n=len(s)
        i=0
        while i < n:
            print(s,i)
            if s[i] not in test:
                sol += hashMap[s[i]]
                i+=1
            else:
                if i>n-2:
                    sol += hashMap[s[i]]
                    i+=1
                    continue
                elif s[i]=="I":
                    if s[i+1]=="V":
                        sol+=4
                        i+=2
                    elif s[i+1]=="X":
                        sol+=9
                        i+=2
                    else:
                        sol += hashMap[s[i]]
                        i+=1
                elif s[i]=="X":
                    if s[i+1]=="L":
                        sol+=40
                        i+=2
                    elif s[i+1]=="C":
                        sol+=90
                        i+=2
                    else:
                        sol += hashMap[s[i]]
                        i+=1
                elif s[i]=="C":
                    if s[i+1]=="D":
                        sol+=400
                        i+=2
                    elif s[i+1]=="M":
                        sol+=900
                        i+=2
                    else:
                        sol += hashMap[s[i]]
                        i+=1
        return sol
