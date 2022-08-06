class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0: 
            return 0

        height = q
        while height < p or height % p:
            height += q

        u = height / p
        r = height / q

        topCorner = 1 if u % 2 else 0

        return topCorner if r % 2 else 2
