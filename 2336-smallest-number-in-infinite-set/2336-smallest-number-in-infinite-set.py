from heapq import heapify,heappush,heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1,1001)]
        self.hashMap={k:True for k in self.h}
        heapify(self.h)

    def popSmallest(self) -> int:
        if len(self.h)==0:
            return None
        m =  heappop(self.h)
        del self.hashMap[m]
        return m

    def addBack(self, num: int) -> None:
        if num not in self.hashMap:
            self.hashMap[num] = True
            heappush(self.h,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)