from collections import defaultdict
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dd=defaultdict(list)
        sol=0
        for x in words:
            dd[x[0]].append(x[1:])
        for i in s:
            li = dd[i]
            dd[i]=[]
            for x in li:
                if not x:
                    sol+=1
                else:
                    dd[x[0]].append(x[1:])
        return sol