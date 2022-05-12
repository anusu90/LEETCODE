from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol=[]
        state = [True]*n
        def bt(curr,hashMap):
            if len(curr)==n:
                temp=curr[:]
                sol.append(temp)
                return
            for num in hashMap:
                if hashMap[num]>0:
                    curr.append(num)
                    hashMap[num]-=1
                    bt(curr,hashMap)
                    curr.pop()
                    hashMap[num]+=1
        bt([],Counter(nums))
        return sol