# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n)==0:
            return n
        s,e=1,n
        while s<=e:
            mid=int((s+e)//2)
            if guess(mid)<0:
                e=mid-1
            elif guess(mid)>0:
                s=mid+1
            else:
                return mid
        