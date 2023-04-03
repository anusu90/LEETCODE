class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        s=0
        e=len(people)-1
        while(s<=e):
            count+=1
            if people[s]+people[e]<=limit:
                s+=1
            e-=1
        return count
            